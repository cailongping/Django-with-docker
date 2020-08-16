from celery import Celery
from django.conf import settings
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hello_django.settings')
app = Celery('hello_django')
app.config_from_object('django.conf:settings',namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS) #只在需要的时候才自动发现任务

@app.task(bind=True)
def debug_task(self):

    print('Request: {0!r}'.format(self.request))