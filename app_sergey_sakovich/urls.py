from django.urls import path

from app_sergey_sakovich.views import helloworld
from app_sergey_sakovich.views import task_money

urlpatterns = [
path("", helloworld),
path("l04/t1", task_money)
]