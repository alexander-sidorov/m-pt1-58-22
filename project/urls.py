from django.contrib import admin
from django.urls import path

from hw.alexander_sidorov.lesson13.views import handle_alexander_sidorov
from hw.eugene_lubimov.lesson13.views import my_view
from hw.jana_sergienko.lesson13.views import handle_jana_sergienko
from hw.vladislav_yurenya.lesson13.views import handle_vladislav_yurenya

urlpatterns = [
    path("admin/", admin.site.urls),
    path("~/alexander_sidorov/", handle_alexander_sidorov),
    path("~/eugene_lubimov/", my_view),
    path("~/jana_sergienko/", handle_jana_sergienko),
    path("~/vladislav_yurenya/", handle_vladislav_yurenya),
]
