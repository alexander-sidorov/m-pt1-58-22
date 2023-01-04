from django.contrib import admin
from django.urls import path

from hw.alexander_sidorov.lesson13.views import handle_alexander_sidorov
from hw.sergey_sakovich.lesson13.views import handle_sergey_sakovich

urlpatterns = [
    path("admin/", admin.site.urls),
    path("~/alexander_sidorov/", handle_alexander_sidorov),
    path("~/sergey_sakovich/", handle_sergey_sakovich),
]
