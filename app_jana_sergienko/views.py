import json

from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render

from hw.jana_sergienko.lesson04.lecture import task_01_money
from hw.jana_sergienko.lesson04.lecture import task_02_sign


def helloworld(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello from app")


def handle_task_01_money(request: HttpRequest) -> HttpResponse:
    if not request.GET:
        return render(request, "app_jana_sergienko/task01.html")

    rub = int(request.GET["r"])
    coin = int(request.GET["c"])
    amt = int(request.GET["a"])
    result = task_01_money(rub, coin, amt)

    payload = {"data": float(result)}

    return HttpResponse(json.dumps(payload), content_type="application/json")


def handle_task_02_sign(request: HttpRequest) -> HttpResponse:
    if request.GET:
        number = int(request.GET["n"])
        result = task_02_sign(number)

    payload = {"data": float(result)}

    return HttpResponse(json.dumps(payload), content_type="application/json")
