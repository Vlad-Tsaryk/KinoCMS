from django.urls import path
from .views import update_user, users, mailing

urlpatterns = [
    path('update/<int:user_id>', update_user, {'admin': True}, name='update_user'),
    path('users/', users, name='users'),
    path('mailing/', mailing, name='mailing'),



]
