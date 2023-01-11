from django.urls import path

from app_eugene_vavilov.views import handle_task_01_money
from app_eugene_vavilov.views import handle_task_02_sign
from app_eugene_vavilov.views import helloworld

urlpatterns = [
    path("", helloworld),
    path("l4/t1/", handle_task_01_money),
    path("l4/t2/", handle_task_02_sign),
]
