# Create your tasks here
from celery import shared_task
import time

@shared_task
def add(x, y):
    time.sleep(3)
    return x + y

@shared_task
def mul(x, y):
    time.sleep(5)
    return x * y

@shared_task
def xsum(numbers):
    time.sleep(10)
    return sum(numbers)

