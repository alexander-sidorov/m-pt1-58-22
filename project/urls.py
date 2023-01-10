from django.contrib import admin
from django.urls import include
from django.urls import path

from hw.alexey_tyuhai.lesson13.views import handle_alexey_tuyhai
from hw.eugene_vavilov.lesson13.views import handle_eugene_vavilov
<<<<<<< HEAD
=======
from hw.maksim_lamaka.lesson13.views import my_view
from hw.mikita_karmanaw.lesson13.views import handle_mikita_karmanaw
>>>>>>> main
from hw.sergey_sakovich.lesson13.views import handle_sergey_sakovich

urlpatterns = [
    path("admin/", admin.site.urls),
    path("~/alexander_sidorov/", include("app_alexander_sidorov.urls")),
    path("~/alexey_tyuhai/", include("app_alexey_tyuhai.urls")),
    path("~/alexey-tuyhai/", handle_alexey_tuyhai),
    path("~/dmitry_mikhailiuk/", include("app_dmitry_mikhailiuk.urls")),
    path("~/eugene_lubimov/", include("app_eugene_lubimov.urls")),
    path("~/eugene_vavilov/", handle_eugene_vavilov),
    path("~/jana_sergienko/", include("app_jana_sergienko.urls")),
    path("~/mikita_karmanaw/", include("app_mikita_karmanaw.urls")),
    path("~/maksim_baranau/", include("app_maksim_baranau.urls")),
    path("~/maksim_lamaka/", my_view),
    path("~/sergey_sakovich/", handle_sergey_sakovich),
    path("~/vadim_zharski/", include("app_vadim_zharski.urls")),
    path("~/vladislav_yurenya/", include("app_vladislav_yurenya.urls")),
]
