from django.urls import path

from app_sergey_sakovich import views


urlpatterns = [
    path("", views.helloworld),
    path("lesson04/task01/", views.handle_task_01_money)
]