from django.urls import path

from app_dmitry_mikhailiuk import views

urlpatterns = [
    path("", views.helloworld),
    path("lesson04/task01/", views.handle_task_01_money),
    path("lesson04/task02/", views.handle_task_02_sign),
    path("lesson04/task03/", views.handle_task_03_triangle),
    path("lesson04/task04/", views.handle_task_04_palindrom),
    path("lesson06/task01/", views.handle_task_01_boundary),
]
