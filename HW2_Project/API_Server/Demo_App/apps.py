from django.apps import AppConfig


class DemoAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Demo_App'

    def ready(self):
        from .LLM_Model import load_model
        load_model()
