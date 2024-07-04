# my_django_project/celery.py
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scr_app.settings')

app = Celery('scr_app')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

# Load task modules from all registered Django app configs.
# app.autodiscover_tasks()

# app.conf.beat_schedule = {
#     #Scheduler Name
#     'print-message-ten-seconds': {
#         # Task Name (Name Specified in Decorator)
#         'task': 'run_spider',  
#         # Schedule      
#         'schedule': 10.0, # seconds
#         # Function Arguments 
#         # 'args': ("Hello",) 
#     },
# }