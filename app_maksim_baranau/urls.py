from django.urls import path

from app_maksim_baranau import views

urlpatterns = [
    path("", views.helloworld),
]