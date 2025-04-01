from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import TransactionDemoModel
from django.db import transaction

@receiver(post_save, sender=TransactionDemoModel)
def transaction_signal_handler(sender, instance, **kwargs):
    print(f"Signal handler transaction: {transaction.get_autocommit()}")
    print(f"Is in atomic block: {transaction.get_autocommit()}")