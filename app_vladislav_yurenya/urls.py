from django.urls import path

from app_vladislav_yurenya import views

urlpatterns = [
    path("", views.helloworld),
    path("lesson04/task01/", views.my_money, name="money"),
    path("lesson04/task02/", views.sign, name="sign"),
    path("lesson04/task03/", views.triangle, name="triangle"),
    path("lesson04/task04/", views.palindrom, name="palindrom"),
    path("lesson04/task_6_01/", views.boundary, name="boundary"),
]
