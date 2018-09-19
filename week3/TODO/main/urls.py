from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.todo_list, name='todo'),
    path('1/completed', views.done_list)
]