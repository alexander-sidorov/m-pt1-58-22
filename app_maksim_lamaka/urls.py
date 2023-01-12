from django.urls import path

from app_maksim_lamaka import views

urlpatterns = [
    path("", views.helloworld),
    path("lesson04/task01/", views.task_money),
    path("lesson04/task04/", views.task_palindrom),
    path("lesson04/task03/", views.task_triangle),
]
