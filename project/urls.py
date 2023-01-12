from django.contrib import admin
from django.urls import include
from django.urls import path

from hw.maksim_lamaka.lesson13.views import my_view

urlpatterns = [
    path("", include("app_main.urls")),
    path("admin/", admin.site.urls),
    path("~/alexander_sidorov/", include("app_alexander_sidorov.urls")),
    path("~/alexey_tyuhai/", include("app_alexey_tyuhai.urls")),
    path("~/dmitry_mikhailiuk/", include("app_dmitry_mikhailiuk.urls")),
    path("~/eugene_lubimov/", include("app_eugene_lubimov.urls")),
    path("~/eugene_vavilov/", include("app_eugene_vavilov.urls")),
    path("~/jana_sergienko/", include("app_jana_sergienko.urls")),
    path("~/maksim_baranau/", include("app_maksim_baranau.urls")),
    path("~/maksim_lamaka/", my_view),
    path("~/mikita_karmanaw/", include("app_mikita_karmanaw.urls")),
    path("~/sergey_sakovich/", include("app_sergey_sakovich.urls")),
    path("~/vadim_zharski/", include("app_vadim_zharski.urls")),
    path("~/vladislav_yurenya/", include("app_vladislav_yurenya.urls")),
]
