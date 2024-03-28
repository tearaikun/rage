from uuid import uuid4

from celery import shared_task
from django.core.mail import send_mail
from django.contrib.auth import get_user_model

from apps.users.models import ConfirmCode

User = get_user_model()

@shared_task
def send_confirm_code(email, user_id):
    user = User.objects.get(id=user_id)
    confirm_code = ConfirmCode.objects.create(
        user=user,
        token=uuid4()
    )
    send_mail(
        subject="Confirm code",
        message=f"Confirm your account http://127.0.0.1:8000/accounts/activation_link?token={confirm_code.token}",
        from_email="artnyr2004@gmail.com",
        recipient_list=[email]
    )
    return confirm_code
    
