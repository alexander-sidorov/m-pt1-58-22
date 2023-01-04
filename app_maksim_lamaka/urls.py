from django.urls import path

from app_maksim_lamaka import views

urlpatterns = [
    path("", views.helloworld),
    path("lesson04/task04/", views.task_money)
]
