from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import ThreadDemoModel
import threading

@receiver(post_save, sender=ThreadDemoModel)
def thread_signal_handler(sender, instance, **kwargs):
    print(f"Signal handler thread: {threading.current_thread().name}")