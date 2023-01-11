from django.urls import path

from app_mikita_karmanaw.views import cities
from app_mikita_karmanaw.views import hdist
from app_mikita_karmanaw.views import hello_mk
from app_mikita_karmanaw.views import money
from app_mikita_karmanaw.views import palindrom
from app_mikita_karmanaw.views import sign
from app_mikita_karmanaw.views import triangle

urlpatterns = [
    path("", hello_mk),
    path("lesson04/task01/", money),
    path("lesson04/task02/", sign),
    path("lesson04/task03/", triangle),
    path("lesson04/task04/", palindrom),
    path("lesson06/task03/", hdist),
    path("lesson06/task04/", cities),
]
