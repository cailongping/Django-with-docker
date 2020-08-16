from django.urls import path
from . import views

app_name='news'
urlpatterns=[
    path('search/', views.course_search, name='course-search'),
    path('index/', views.index, name='index'),
    path('test/', views.task_test, name='test'),
]