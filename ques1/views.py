from django.http import HttpResponse
from .models import DemoModel
import time

def test_view(request):
    print("View execution started")
    DemoModel.objects.create(name="Test")
    print("View execution completed")
    return HttpResponse("Check your console output")