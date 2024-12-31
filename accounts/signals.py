# accounts/signals.py
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(pre_save, sender=User)
def set_first_name_uppercase(sender, instance, **kwargs):
    # Automatically convert the first_name to uppercase
    if instance.first_name:
        instance.first_name = instance.first_name.upper()
