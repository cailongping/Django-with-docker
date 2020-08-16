from django.urls import path
from . import views

app_name='music'
urlpatterns=[
    path('sendmsg/',views.send_msg,name='send_msg')
]