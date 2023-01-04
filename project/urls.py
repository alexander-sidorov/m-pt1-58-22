from django.contrib import admin
from django.urls import path

from hw.jana_sergienko.lesson13.views import handle_jana_sergienko

urlpatterns = [
    path("admin/", admin.site.urls),
    path("~/jana_sergienko/", handle_jana_sergienko),
]
