from celery import shared_task
from django.core.mail import send_mail
from KinoCMS.settings import EMAIL_HOST
from time import sleep


@shared_task
def sleepy(duration):
    sleep(duration)
    return None


@shared_task
def send_mail_task(msg_title, html_message, emails_list: list):
    send_mail(
        subject=msg_title,
        message=msg_title,
        from_email=EMAIL_HOST,
        recipient_list=emails_list,
        html_message=html_message
        )
