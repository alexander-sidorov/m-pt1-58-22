from django.urls import path

from app_mikita_karmanaw.views import hello_mk

urlpatterns = [
    path("", hello_mk),
]
