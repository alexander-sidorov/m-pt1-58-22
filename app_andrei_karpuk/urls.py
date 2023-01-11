from django.urls import path

from app_andrei_karpuk import views

urlpatterns = [
    path("", views.helloworld_ak),
    path("lesson04/task01/", views.task_money),
    path("lesson04/task02/", views.task_sign),
]
