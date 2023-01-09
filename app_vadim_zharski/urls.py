from django.urls import path

from app_vadim_zharski import views

app_name = "app_vadim_zharski"

urlpatterns = [
    path("", views.hello_world_vadim_zharski, name="hello"),
    path("lesson04/task01/", views.task_money, name="task_money"),
]
