from django.shortcuts import render
from django.http import HttpResponse
from . import tasks
import random

# Create your views here.
def send_msg(request):
    msg_num="%06d" % random.randint(0,999999)
    tasks.send_message.delay(mobile='15989502326',msg=msg_num,expires=3)

    return HttpResponse('send messages success')