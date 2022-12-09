from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from django.conf import settings
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE','Magallanes.settings' )

app = Celery('Magallanes')
app.conf.enable_utc = False

app.conf.update(timezone = 'America/Argentina/Buenos_Aires')

app.config_from_object(settings, namespace='CELERY')

#Celery Beat Settings
app.conf.beat_schedule={
    'send-mail-everyday-at-8pm':{
        'task' : 'store_app.tasks.send_mail_func',
        'schedule' : crontab(hour=1, minute=16),
    }

}

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')