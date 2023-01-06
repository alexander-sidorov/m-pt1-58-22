from django.urls import path

from app_eugene_vavilov.views import helloworld
from app_eugene_vavilov.views import handle_task_01_money

urlpatterns = [
path("", helloworld),
path("l4/t1/", handle_task_01_money)
]