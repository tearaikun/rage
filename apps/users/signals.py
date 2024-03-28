from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

from apps.users.tasks import send_confirm_code

User = get_user_model()

@receiver(post_save, sender=User)
def send_confirm_message(sender, instance, created, **kwargs):
    if created:
        send_confirm_code.delay(email=instance.email, user_id=instance.id)