from celery import shared_task
from time import sleep
from django.core.mail import send_mail
from task_manager.settings.base import EMAIL_HOST_USER


@shared_task
def user_verification_email(user_email, token):
    print('hello from celery')

    subject= 'Email registration'
    message = f'''click on link bellow to finish your registration -> 
                http://localhost:8000/users/verify-email/?token={token}'''

    x = send_mail(
        subject,
        message,
        EMAIL_HOST_USER,
        [user_email],
        fail_silently=False,
    )