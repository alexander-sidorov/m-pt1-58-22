from django.contrib import admin
from django.urls import path
from hw.eugene_vavilov.lesson13.lesson import handle_eugene_vavilov

from hw.alexander_sidorov.lesson13.views import handle_alexander_sidorov

urlpatterns = [
    path("admin/", admin.site.urls),
    path("~/alexander_sidorov/", handle_alexander_sidorov),
    path("~/handle_eugene_vavilov/", handle_eugene_vavilov)
]