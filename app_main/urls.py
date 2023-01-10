from django.urls import path

from app_main.views import main

urlpatterns = [
    path("", main),
]
