from django.apps import AppConfig

class SyncVsAsyncConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ques3'

    def ready(self):
        import ques3.singals