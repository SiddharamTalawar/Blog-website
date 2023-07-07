from celery import shared_task
from .email import send_mail

@shared_task()
def send_mail_task(user):
    a = send_mail(user)  