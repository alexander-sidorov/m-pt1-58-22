from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render

list_students = [
    "alexander_sidorov",
    "alexey_tyuhai",
    "andrei_karpuk",
    "dmitry_mikhailiuk",
    "eugene_bakun",
    "eugene_ladyko",
    "eugene_lubimov",
    "eugene_vavilov",
    "igor_maksimov",
    "jana_sergienko",
    "maksim_baranau",
    "maksim_lamaka",
    "mikita_karmanaw",
    "sergey_sakovich",
    "vadim_zharski",
    "vladislav_yurenya",
]


def liststudents(request: HttpRequest) -> HttpResponse:
    return render(
        request, "app_main/index.html", {"list_students": list_students}
    )
