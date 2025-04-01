# **AccuKnox Django Trainee**  
Assignment for Django Trainee  

## **Answers to Questions**  

### **Question 1: Are Django signals synchronous or asynchronous?**  
Django signals are executed **synchronously** by default. When a signal is sent, all registered receivers are called immediately in sequence, and the calling code **blocks** until all signal handlers complete execution.  

#### **Example**  
```python
import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import DemoModel

@receiver(post_save, sender=DemoModel)
def sync_signal_handler(sender, instance, **kwargs):
    print("Signal handler started")
    time.sleep(2)  # Blocking operation
    print("Signal handler completed")
```

#### **Console Output**  
```
View execution started  
Signal handler started  # ← View pauses here  
Signal handler completed  
View execution completed  # ← Resumes after signal  
```

---

### **Question 2: Do Django signals run in the same thread as the caller?**  
Yes, Django signals run **in the same thread** as the caller because Django’s WSGI server processes requests synchronously.  

#### **Example**  
```python
import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import ThreadDemoModel

@receiver(post_save, sender=ThreadDemoModel)
def handler(sender, instance, **kwargs):
    print(f"Signal thread: {threading.current_thread().name}")
```

#### **Console Output**  
```
View thread: Thread-1 (process_request_thread)  
Signal thread: Thread-1 (process_request_thread)  # ← Matching IDs confirm the same thread  
```

---

### **Question 3: Do Django signals run in the same database transaction as the caller?**  
Yes, Django signals **operate in the same transaction** as the caller because:  
- Django **wraps views in transactions by default**  
- Data integrity requires **atomic** operations  
- Signal handlers should **commit/rollback** together with the main operation  

#### **Example**  
```python
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import transaction
from .models import TransactionDemoModel

@receiver(post_save, sender=TransactionDemoModel)
def handler(sender, instance, **kwargs):
    print(f"Signal atomic: {transaction.get_autocommit()}")
```

#### **Console Output**  
```
View outside: autocommit=True  
View in transaction: autocommit=False  
Signal in transaction: autocommit=False  # ← Inherits transaction context  
View after: autocommit=True  
```

### **Question 4: answer is in ques4.py file **

---

## **Setup Instructions**  

### **1. Clone the repository:**  
```bash
git clone https://github.com/yourusername/accuknox_django_trainee.git
cd accuknox_django_trainee
```

### **2. Create a virtual environment and activate it:**  
```bash
python -m venv venv  
source venv/bin/activate  # On Windows: venv\Scripts\activate  
```

### **3. Install Django:**  
```bash
pip install django
```

### **4. Apply migrations:**  
```bash
python manage.py migrate
```

### **4. Run server:**  
```bash
python manage.py runserver
```

---

## **Running the Tests**  

 Test each question by hitting the API endpoints:

Question 1:  http://127.0.0.1:8000/ques1/

Question 2:  http://127.0.0.1:8000/ques2/

Question 3:  http://127.0.0.1:8000/ques3/

