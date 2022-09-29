from django.urls import path
from .views import update_user, users, mailing

urlpatterns = [
    path('update/<int:user_id>', update_user, name='update_user'),
    path('users/', users, name='users'),
    path('mailing/', mailing, name='mailing'),



]
