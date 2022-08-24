from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from .models import User
from .forms import CustomUserChangeForm


# Create your views here.

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('films')
    context = {}
    return render(request, 'users/login.html', context)


def update_user(request, user_id):
    obj_user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        user_change_form = CustomUserChangeForm(request.POST, instance=obj_user)
        if user_change_form.is_valid():
            user = user_change_form.save(commit=False)
            user.save()
    else:
        user_change_form = CustomUserChangeForm(instance=obj_user)

    context = {}
    return render(request, 'users/user_update.html', context)
