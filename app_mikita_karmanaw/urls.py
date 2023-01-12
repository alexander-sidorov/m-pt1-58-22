from django.urls import path

from app_mikita_karmanaw.views import hello_mk
from app_mikita_karmanaw.views import money

urlpatterns = [
    path("", hello_mk, name="karmaxa_main"),
    path("lesson04/task01/", money, name="karmaxa_task_money"),
]
