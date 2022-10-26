from django.urls import path
from .views import update_user, users, mailing, delete_email, delete_user

urlpatterns = [
    path('update/<int:user_id>', update_user, {'admin': True}, name='update_user'),
    path('users/', users, name='users'),
    path('mailing/', mailing, name='mailing'),
    path('delete_user/<int:user_id>', delete_user, name='delete_user'),
    path('delete_template/<int:template_id>', delete_email, name='delete_template'),



]
