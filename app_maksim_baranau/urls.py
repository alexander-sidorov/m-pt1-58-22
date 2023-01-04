from django.urls import path

from app_maksim_baranau import views

urlpatterns = [
    path("", views.helloworld),
    path("lesson04/task_01/",views.handle_task_01_money),
]