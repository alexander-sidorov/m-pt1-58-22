from django.urls import path

from app_alexey_tyuhai import views

urlpatterns = [
    path("", views.hello),
    path("lesson04/task01/", views.handle_task_01_money),
]
