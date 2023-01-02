from django.contrib import admin
from django.urls import path

from hw.alexander_sidorov.lesson13.views import handle_alexander_sidorov
from hw.dmitry_mihkailiuk.lesson13.views import handle_dmitry_mikhailiuk

urlpatterns = [
    path("admin/", admin.site.urls),
    path("~/alexander_sidorov/", handle_alexander_sidorov),
    path("~/dmitry_mihkailiuk/", handle_dmitry_mikhailiuk),
]
