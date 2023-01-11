from django.urls import path

from app_mikita_karmanaw.views import cities
from app_mikita_karmanaw.views import hdist
from app_mikita_karmanaw.views import hello_mk
from app_mikita_karmanaw.views import money
from app_mikita_karmanaw.views import palindrom
from app_mikita_karmanaw.views import route
from app_mikita_karmanaw.views import sign
from app_mikita_karmanaw.views import triangle

urlpatterns = [
    path("", hello_mk, name="karmaxa_main"),
    path("lesson04/task01/", money, name="karmaxa_money"),
    path("lesson04/task02/", sign, name="karmaxa_sign"),
    path("lesson04/task03/", triangle, name="karmaxa_triangle"),
    path("lesson04/task04/", palindrom, name="karmaxa_palindrom"),
    path("lesson06/task03/", hdist, name="karmaxa_hdist"),
    path("lesson06/task04/", cities, name="karmaxa_cities"),
    path("lesson06/task05/", route, name="karmaxa_route"),
]
