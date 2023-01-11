from django.urls import path

from app_maksim_baranau import views

urlpatterns = [
    path("", views.helloworld),
    path("lesson04/task_01/", views.handle_task_01_money),
    path("lesson04/task_02/", views.handle_task_02_sign),
    path("lesson04/task_03/", views.handle_task_03_triangle),
    path("lesson04/task_04/", views.handle_task_04_palindrom),
]
