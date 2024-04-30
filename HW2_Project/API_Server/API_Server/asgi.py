"""
ASGI config for API_Server project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

# import os

# from django.core.asgi import get_asgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'API_Server.settings')

# application = get_asgi_application()


import os
from django.core.asgi import get_asgi_application
from Demo_App.LLM_Model import load_model 

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'API_Server.settings')
django_asgi_app = get_asgi_application()
load_model()  

application = django_asgi_app
