from django.urls import path

from app_eugene_vavilov.views import handle_task_01_money
from app_eugene_vavilov.views import handle_task_02_sign
from app_eugene_vavilov.views import handle_task_03_triangle
from app_eugene_vavilov.views import handle_task_04_palindrom
from app_eugene_vavilov.views import helloworld

urlpatterns = [
    path("", helloworld),
    path("l4/t1/", handle_task_01_money),
    path("l4/t2/", handle_task_02_sign),
    path("l4/t3/", handle_task_03_triangle),
    path("l4/t4/", handle_task_04_palindrom),
]
