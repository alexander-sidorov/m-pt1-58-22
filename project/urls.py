from django.contrib import admin
from django.urls import path

from hw.alexander_sidorov.lesson13.views import handle_alexander_sidorov
from hw.dmitry_mihkailiuk.lesson13.views import handle_dmitry_mikhailiuk
from hw.eugene_lubimov.lesson13.views import my_view
from hw.jana_sergienko.lesson13.views import handle_jana_sergienko
from hw.mikita_karmanaw.lesson13.views import handle_mikita_karmanaw
from hw.vadim_zharski.lesson13.views import handle_vadim_zharski
from hw.vladislav_yurenya.lesson13.views import handle_vladislav_yurenya

urlpatterns = [
    path("admin/", admin.site.urls),
    path("~/alexander_sidorov/", handle_alexander_sidorov),
    path("~/dmitry_mihkailiuk/", handle_dmitry_mikhailiuk),
    path("~/eugene_lubimov/", my_view),
    path("~/jana_sergienko/", handle_jana_sergienko),
    path("~/mikita_karmanaw/", handle_mikita_karmanaw),
    path("~/vadim_zharski", handle_vadim_zharski),
    path("~/vladislav_yurenya/", handle_vladislav_yurenya),
]
