from django.urls import path

from app_mikita_karmanaw.views import hello_mk
from app_mikita_karmanaw.views import l04t01_money
from app_mikita_karmanaw.views import l04t02_sign
from app_mikita_karmanaw.views import l04t03_triangle
from app_mikita_karmanaw.views import l04t04_palindrom
from app_mikita_karmanaw.views import l06t03_hdist
from app_mikita_karmanaw.views import l06t04_cities
from app_mikita_karmanaw.views import l06t05_route

app_name = "karmaxa"

urlpatterns = [
    path("", hello_mk, name="index"),
    path("lesson04/task01/", l04t01_money, name="money"),
    path("lesson04/task02/", l04t02_sign, name="sign"),
    path("lesson04/task03/", l04t03_triangle, name="triangle"),
    path("lesson04/task04/", l04t04_palindrom, name="palindrom"),
    path("lesson06/task03/", l06t03_hdist, name="hdist"),
    path("lesson06/task04/", l06t04_cities, name="cities"),
    path("lesson06/task05/", l06t05_route, name="route"),
]
