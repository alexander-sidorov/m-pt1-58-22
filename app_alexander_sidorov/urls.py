from django.urls import path

from app_alexander_sidorov import views

urlpatterns = [
    path("", views.index),
    path("api/04/01/", views.handle_04_01_money),
    path("api/04/02/", views.handle_04_02_sign),
    path("api/04/03/", views.handle_04_03_triangle),
    path("api/04/04/", views.handle_04_04_palindrome),
]
