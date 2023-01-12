from django.urls import path

from app_eugene_lubimov import views

urlpatterns = [
    path("", views.helloworld),
    path("lesson04/task01/", views.handle_task_money),
    path("lesson04/task02/", views.handle_task_02_sign),
    path("lesson04/task03/", views.handle_task_03_triangle),
    path("lesson04/task04/", views.handle_task_04_palindrom),
    path("lesson04/task05/", views.handle_task_01_boundary),
    path("lesson04/task06/", views.handle_task_02_expand),
    path("lesson04/task07/", views.handle_task_03_hdist),
]
