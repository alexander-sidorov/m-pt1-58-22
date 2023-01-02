from django.contrib import admin
from django.urls import path

from hw.dmitry_mihkailiuk.lesson13.views import handle_dmitry_mikhailiuk

urlpatterns = [
    path("admin/", admin.site.urls),
    path("~/dmitry_mihkailiuk/", handle_dmitry_mikhailiuk),
]
