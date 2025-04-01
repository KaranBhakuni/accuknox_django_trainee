from django.http import HttpResponse
from .models import ThreadDemoModel
import threading

def test_view(request):
    print(f"View thread: {threading.current_thread().name}")
    ThreadDemoModel.objects.create(name="Test")
    return HttpResponse("Check your console output")


