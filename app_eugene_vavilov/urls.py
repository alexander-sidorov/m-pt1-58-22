from django.urls import path

from app_eugene_vavilov.views import handle_task_01_boudary
from app_eugene_vavilov.views import handle_task_01_money
from app_eugene_vavilov.views import handle_task_02_expand
from app_eugene_vavilov.views import handle_task_02_sign
from app_eugene_vavilov.views import handle_task_03_hdist
from app_eugene_vavilov.views import handle_task_03_triangle
from app_eugene_vavilov.views import handle_task_04_cities
from app_eugene_vavilov.views import handle_task_04_palindrom
from app_eugene_vavilov.views import handle_task_05_route
from app_eugene_vavilov.views import helloworld

urlpatterns = [
    path("", helloworld),
    path("l4/t1/", handle_task_01_money),
    path("l4/t2/", handle_task_02_sign),
    path("l4/t3/", handle_task_03_triangle),
    path("l4/t4/", handle_task_04_palindrom),
    path("l6/t1/", handle_task_01_boudary),
    path("l6/t2/", handle_task_02_expand),
    path("l6/t3/", handle_task_03_hdist),
    path("l6/t4/", handle_task_04_cities),
    path("l6/t5/", handle_task_05_route),
]
