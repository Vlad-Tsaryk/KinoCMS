from django.urls import path
from .views import login_page, update_user, create_user,logout_user, users

urlpatterns = [
    path('login/', login_page, name='login_page'),
    path('update/<int:user_id>', update_user, name='update_user'),
    path('register/', create_user, name='register'),
    path('logout/', logout_user, name='logout'),
    path('users/', users, name='users'),


]
