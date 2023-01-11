from django.urls import path

from app_eugene_bakun import views

urlpatterns = [
    path("", views.helloworld),
]
