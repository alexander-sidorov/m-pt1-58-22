from django.urls import path

from app_vadim_zharski import views

urlpatterns = [
    path("", views.hello_world_vadim_zharski),
    path("lesson04/task01/", views.task_money),
]
