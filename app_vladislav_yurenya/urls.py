from django.urls import path

from app_vladislav_yurenya import views

urlpatterns = [
    path("", views.helloworld),
]