from django.contrib import admin
from django.urls import path

from hw.alexander_sidorov.lesson13.views import handle_alexander_sidorov
from hw.eugene_vavilov.lesson13.views import handle_eugene_vavilov

urlpatterns = [
    path("admin/", admin.site.urls),
    path("~/alexander_sidorov/", handle_alexander_sidorov),
    path("~/eugene_vavilov/", handle_eugene_vavilov),
]
