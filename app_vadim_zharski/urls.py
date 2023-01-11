from django.urls import path

from app_vadim_zharski import views

app_name = "app_vadim_zharski"

urlpatterns = [
    path("", views.hello_world_vadim_zharski, name="hello"),
    path("lesson04/task01/", views.task_money, name="task_money"),
    path("lesson04/task02", views.task_sign, name="task_sign"),
    path("lesson04/task03", views.task_triangle, name="task_triangle"),
    path("lesson04/task04", views.task_palindrom, name="task_palindrom"),
    path("lesson06/task01", views.task_06_boundary, name="task_boundary"),
]
