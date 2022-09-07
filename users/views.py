from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import User
from .forms import CustomUserChangeForm, CustomUserCreationForm, MailingFormSet


# Create your views here.

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('films')
        else:
            messages.info(request, 'Username OR Password is incorrect')
    context = {}
    return render(request, 'users/login.html', context)


@login_required(login_url='login_page')
def update_user(request, user_id):
    obj_user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        user_change_form = CustomUserChangeForm(request.POST, instance=obj_user)
        if user_change_form.is_valid():
            user = user_change_form.save(commit=False)
            user.save()
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
    return redirect('login_page')


def users(request):
    obj_users = User.objects.all()
    context = {'users': obj_users}
    return render(request, 'users/users.html', context)


def mailing(request):
    if request.method == 'POST':
        mailing_formset = MailingFormSet(request.POST, request.FILES)
        if mailing_formset.is_valid():
            mails = mailing_formset.save(commit=False)

            for del_mail in mails.deleted_objects:
                print(del_mail)
                del_mail.delete()

            mails.save()
            return redirect('mailing')
    else:
        mailing_formset = MailingFormSet()
    context = {'mailing_formset': mailing_formset}
    return render(request, 'users/mailing.html', context)


def user_choice(request):
    obj_users = User.objects.all()
    context = {'users': obj_users}
    return render(request, 'users/users_choice.html', context)
