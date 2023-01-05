from django.contrib import admin
from django.urls import include
from django.urls import path

from hw.alexander_sidorov.lesson13.views import handle_alexander_sidorov
from hw.alexey_tyuhai.lesson13.hello_world import handle_alexey_tuyhai
from hw.andrei_karpuk.lesson13.views import ak_view
from hw.dmitry_mihkailiuk.lesson13.views import handle_dmitry_mikhailiuk
from hw.eugene_lubimov.lesson13.views import my_view
from hw.eugene_vavilov.lesson13.views import handle_eugene_vavilov
from hw.mikita_karmanaw.lesson13.views import handle_mikita_karmanaw
from hw.sergey_sakovich.lesson13.views import handle_sergey_sakovich
from hw.vadim_zharski.lesson13.views import handle_vadim_zharski
from hw.vladislav_yurenya.lesson13.views import handle_vladislav_yurenya

urlpatterns = [
    path("admin/", admin.site.urls),
    path("~/alexander_sidorov/", handle_alexander_sidorov),
    path("~/alexander_sidorov/", handle_alexander_sidorov),
    path("~/alexey-tuyhai/", handle_alexey_tuyhai),
    path("~/andrei_karpuk/", ak_view),
    path("~/dmitry_mihkailiuk/", handle_dmitry_mikhailiuk),
    path("~/eugene_lubimov/", my_view),
    path("~/eugene_vavilov/", handle_eugene_vavilov),
    path("~/jana_sergienko/", include("app_jana_sergienko.urls")),
    path("~/maksim_lamaka/", my_view),
    path("~/mikita_karmanaw/", handle_mikita_karmanaw),
    path("~/sergey_sakovich/", handle_sergey_sakovich),
    path("~/vadim_zharski", handle_vadim_zharski),
    path("~/vladislav_yurenya/", handle_vladislav_yurenya),
]
