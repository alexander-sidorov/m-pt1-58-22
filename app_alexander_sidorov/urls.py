from django.urls import path

from app_alexander_sidorov import views

urlpatterns = [
    path("", views.helloworld),
]
