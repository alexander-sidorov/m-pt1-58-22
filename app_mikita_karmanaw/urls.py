from django.urls import path

from app_mikita_karmanaw.views import hello_mk, money

urlpatterns = [
    path("", hello_mk),
    path("money", money),
]
