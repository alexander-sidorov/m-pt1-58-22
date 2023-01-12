import json

from django.http import HttpRequest
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render

list_students = [
    "alexander_sidorov",
    "alexey_tyuhai",
    "andrei_karpuk",
    "dmitry_mihkailiuk",
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
listdict_students = [{"name": student} for student in list_students]


def liststudents(request: HttpRequest) -> HttpResponse:
    return render(
        request, "app_main/index.html", {"list_students": list_students}
    )


def students_listdict(request: HttpRequest) -> HttpResponse:
    payload = {"data": {"students": listdict_students}}
    return JsonResponse(payload)
