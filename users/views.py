from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import User, Mail_template
from .forms import CustomUserChangeForm, CustomUserCreationForm, MailingForm
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
            if request.GET.get('next') and request.user.is_superuser:
                print('next found')
                return redirect('/' + user.language + request.GET.get('next')[3:])
            else:
                return redirect('kino_cms')
        else:
            messages.info(request, 'Username OR Password is incorrect')
    context = {}
    return render(request, 'users/login.html', context)


@login_required()
# @user_passes_test(lambda u: u.is_superuser)
def update_user(request, user_id, admin):
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
    if admin:
        return render(request, 'users/user_update.html', context)
    else:
        return render(request, 'users/site_user_update.html', context)


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
    mails = Mail_template.objects.all()
    if request.method == 'POST':
        mail_form = MailingForm(request.POST, request.FILES)
        print(request.POST)
        # print(mail_form.template)
        send_mail = request.POST.get('send_email')
        if send_mail:
            if send_mail == 'file':
                mail = mail_form.save()
                do_mailing(mail, request, obj_users)
                return redirect('mailing')
            else:
                template_obj = Mail_template.objects.get(pk=send_mail)
                do_mailing(template_obj, request, obj_users)
                return redirect('mailing')
        else:
            print('not valid')
    else:
        mail_form = MailingForm()
    context = {'users': obj_users, 'mails': mails, 'mail_form': mail_form}
    return render(request, 'users/mailing.html', context)


def do_mailing(template_obj, request, obj_users):
    with open(template_obj.template.path, 'r') as f:
        html_message = f.read()
    emails_list = []
    if request.POST.get('all_users'):
        emails_list = []
        for user in obj_users:
            emails_list.append(user.email)
        send_mail_task(msg_title='KinoCMS', html_message=html_message, emails_list=emails_list)
    if request.POST.get('user_choice'):
        emails_list = request.POST.getlist('users_email')
        if emails_list:
            print('sending.....')
            print(emails_list)
            send_mail_task(msg_title='KinoCMS', html_message=html_message, emails_list=emails_list)


@login_required()
@user_passes_test(lambda u: u.is_superuser)
def delete_email(request, template_id):
    del_template = Mail_template.objects.get(pk=template_id)
    del_template.delete()
    return redirect('mailing')


@login_required()
@user_passes_test(lambda u: u.is_superuser)
def delete_user(request, user_id):
    del_user = User.objects.get(pk=user_id)
    if not del_user.is_superuser:
        del_user.delete()
    return redirect('users')
