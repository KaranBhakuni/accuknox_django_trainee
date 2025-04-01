from django.http import HttpResponse
from .models import TransactionDemoModel
from django.db import transaction

def test_view(request):
    with transaction.atomic():
        print(f"View transaction: {transaction.get_autocommit()}")
        print(f"Is in atomic block: {transaction.get_autocommit()}")
        TransactionDemoModel.objects.create(name="Test")
    return HttpResponse("Check your console output")