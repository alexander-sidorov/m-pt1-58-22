from django.contrib import admin
from django.urls import path, include


from hw.alexey_tyuhai.lesson13.hello_world import handle_alexey_tuyhai
from hw.dmitry_mihkailiuk.lesson13.views import handle_dmitry_mikhailiuk
from hw.eugene_lubimov.lesson13.views import my_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("~/alexey-tuyhai/", handle_alexey_tuyhai),
    path("~/dmitry_mihkailiuk/", handle_dmitry_mikhailiuk),
    path("~/eugene_lubimov/", my_view),
    path("~/maksim_lamaka/", include("app_maksim_lamaka.urls")),
]
