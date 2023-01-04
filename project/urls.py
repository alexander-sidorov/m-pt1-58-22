from django.contrib import admin
from django.urls import include
from django.urls import path

from hw.alexander_sidorov.lesson13.views import handle_alexander_sidorov
from hw.alexey_tyuhai.lesson13.hello_world import handle_alexey_tuyhai
from hw.dmitry_mihkailiuk.lesson13.views import handle_dmitry_mikhailiuk
from hw.eugene_lubimov.lesson13.views import my_view
from hw.eugene_vavilov.lesson13.views import handle_eugene_vavilov
from hw.jana_sergienko.lesson13.views import handle_jana_sergienko
from hw.sergey_sakovich.lesson13.views import handle_sergey_sakovich
from hw.vadim_zharski.lesson13.views import handle_vadim_zharski
from hw.vladislav_yurenya.lesson13.views import handle_vladislav_yurenya

urlpatterns = [
    path("admin/", admin.site.urls),
    path("~/alexander_sidorov/", handle_alexander_sidorov),
    path("~/alexey-tuyhai/", handle_alexey_tuyhai),
    path("~/dmitry_mihkailiuk/", handle_dmitry_mikhailiuk),
    path("~/eugene_lubimov/", my_view),
    path("~/eugene_vavilov/", handle_eugene_vavilov),
    path("~/jana_sergienko/", handle_jana_sergienko),
    path("~/mikita_karmanaw/", include("app_mikita_karmanaw.urls")),
    path("~/sergey_sakovich/", handle_sergey_sakovich),
    path("~/vadim_zharski", handle_vadim_zharski),
    path("~/vladislav_yurenya/", handle_vladislav_yurenya),
]
