from django.contrib import admin
from django.urls import path
from hw.dmitry_mihkailiuk.lesson13.hello_world import handle_dmitry_mikhailiuk

urlpatterns = [
    path("admin/", admin.site.urls),
    path("dmitry-mikhailiuk/", handle_dmitry_mikhailiuk),

]
