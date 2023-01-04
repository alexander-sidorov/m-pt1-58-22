from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("~/dmitry_mikhailiuk/", include("app_dmitry_mikhailiuk.urls")),
]
