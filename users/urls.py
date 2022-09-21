from django.urls import path
from .views import update_user, users, mailing, user_choice, test_mail

urlpatterns = [
    path('update/<int:user_id>', update_user, name='update_user'),
    path('users/', users, name='users'),
    path('mailing/', mailing, name='mailing'),
    path('mailing/users', user_choice, name='user_choice'),
    path('test/', test_mail, name='test_mail'),



]
