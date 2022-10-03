from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import User, Mail_template
from .forms import CustomUserChangeForm, CustomUserCreationForm, MailingFormSet
from .tasks import send_mail_task
from django.utils import translation


# Create your views here.

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print(request.POST)
        # print(request.GET.get('next'))

        if user is not None:
            login(request, user)
            print(user.language)
            translation.activate(user.language)
            request.LANGUAGE_CODE = user.language
            if request.GET.get('next'):
                print('next found')
                return redirect('/' + user.language + request.GET.get('next')[3:])
            else:
                return redirect('kino_cms')
        else:
            messages.info(request, 'Username OR Password is incorrect')
    context = {}
    return render(request, 'users/login.html', context)


@login_required()
@user_passes_test(lambda u: u.is_superuser)
def update_user(request, user_id):
    obj_user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        user_change_form = CustomUserChangeForm(request.POST, instance=obj_user)
        if user_change_form.is_valid():
            user = user_change_form.save(commit=False)
            user.save()
            translation.activate(user.language)
            request.LANGUAGE_CODE = user.language
            return redirect('users')
    else:
        user_change_form = CustomUserChangeForm(instance=obj_user)

    context = {'user_form': user_change_form}
    return render(request, 'users/user_update.html', context)


def create_user(request):
    if request.user.is_authenticated:
        return redirect('')
    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(request.POST)
        if user_creation_form.is_valid():
            user = user_creation_form.save(commit=False)
            user.save()
            messages.success(request, 'User "' + user.username + '" create successful')
            return redirect('login_page')
    else:
        user_creation_form = CustomUserCreationForm()

    context = {'user_form': user_creation_form}
    return render(request, 'users/register.html', context)


def logout_user(request):
    logout(request)
    return redirect(request.META['HTTP_REFERER'])


@login_required()
@user_passes_test(lambda u: u.is_superuser)
def users(request):
    obj_users = User.objects.all()
    context = {'users': obj_users}
    return render(request, 'users/users.html', context)


@login_required()
@user_passes_test(lambda u: u.is_superuser)
def mailing(request):
    obj_users = User.objects.all()
    if request.method == 'POST':
        mailing_formset = MailingFormSet(request.POST, request.FILES)
        print(request.POST)
        if mailing_formset.is_valid():
            mails = mailing_formset.save(commit=False)
            for del_mail in mailing_formset.deleted_objects:
                print(del_mail)
                del_mail.delete()

            for mail in mails:
                mail.save()
            mail_test = Mail_template.objects.get(pk=request.POST.get('template'))
            with open(mail_test.template.path, 'r') as f:
                html_message = f.read()
            emails_list = []
            if request.POST.get('all_users'):
                emails_list = []
                for user in obj_users:
                    emails_list.append(user.email)
                print(emails_list)

                send_mail_task(msg_title='KinoCMS', html_message=html_message, emails_list=emails_list)
            if request.POST.get('user_choice'):
                emails_list = request.POST.getlist('users_email')
                if emails_list:
                    print('sending.....')
                    print(emails_list)
                    send_mail_task(msg_title='KinoCMS', html_message=html_message, emails_list=emails_list)

            return redirect('mailing')
        else:
            print('not valid')
    else:
        mailing_formset = MailingFormSet()
    context = {'mailing_formset': mailing_formset, 'users': obj_users}
    return render(request, 'users/mailing.html', context)
