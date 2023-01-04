from django.contrib import admin
from django.urls import path

from hw.alexander_sidorov.lesson13.views import handle_alexander_sidorov
from hw.jana_sergienko.lesson13.views import handle_jana_sergienko

urlpatterns = [
    path("admin/", admin.site.urls),
    path("~/alexander_sidorov/", handle_alexander_sidorov),
]

urlpatterns = [
    path("admin/", admin.site.urls),
    path("~/jana_sergienko/", handle_jana_sergienko),
]
