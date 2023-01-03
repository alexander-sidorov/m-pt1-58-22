from django.urls import path

from hw.alexander_sidorov.lesson13.views import handle_alexander_sidorov
from hw.andrei_karpuk.lesson13.views import my_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("~/alexander_sidorov/", handle_alexander_sidorov),
    path("~/andrei_karpuk/", my_view),
]
