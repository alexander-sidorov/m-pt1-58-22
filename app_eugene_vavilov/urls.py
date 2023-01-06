from django.urls import path

from app_eugene_vavilov.views import handle_task_01_money
from app_eugene_vavilov.views import helloworld

urlpatterns = [  # noqa
    path("", helloworld),  # noqa
    path("l4/t1/", handle_task_01_money)  # noqa
]
