from django.urls import path

from app_jana_sergienko import views

urlpatterns = [
    path("", views.helloworld),
]
