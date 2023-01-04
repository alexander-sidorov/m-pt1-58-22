from django.urls import path

from app_eugene_ladyko import views

urlpatterns = [
    path("", views.helloworld),
]
