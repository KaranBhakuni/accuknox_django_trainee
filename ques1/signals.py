from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import DemoModel
import time

@receiver(post_save, sender=DemoModel)
def sync_signal_handler(sender, instance, **kwargs):
    print("Signal handler started")
    time.sleep(2)  # Blocking operation
    print("Signal handler completed")