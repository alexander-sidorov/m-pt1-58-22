from django.urls import path

from app_eugene_lubimov import views

urlpatterns = [
    path("", views.helloworld),
    path("lesson04/task01/", views.handle_task_money),
]
