import json

from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render

from hw.sergey_sakovich.lesson04.lecture import task_01_money
from hw.sergey_sakovich.lesson04.lecture import task_02_sign
from hw.sergey_sakovich.lesson04.lecture import task_03_triangle
from hw.sergey_sakovich.lesson04.lecture import task_04_palindrom


def helloworld(request: HttpRequest) -> HttpResponse:
    return HttpResponse("HELLO FROM APP!")


def handle_task_01_money(request: HttpRequest) -> HttpResponse:

    if request.GET:
        rubles = int(request.GET["r"])
        coins = int(request.GET["c"])
        amount = int(request.GET["a"])
        result = task_01_money(rubles, coins, amount)

    return render(
        request, "app_sergey_sakovich/task01.html", {"result": result}
    )


def handle_task_02_sign(request: HttpRequest) -> HttpResponse:

    if request.GET:
        number = int(request.GET["i"])
        result = task_02_sign(number)

    payload = {
        "data": int(result),
    }

    return HttpResponse(json.dumps(payload), content_type="application/json")


def handle_task_03_triangle(request: HttpRequest) -> HttpResponse:

    if request.GET:
        side1 = float(request.GET["a"])
        side2 = float(request.GET["b"])
        side3 = float(request.GET["c"])
        result = task_03_triangle(side1, side2, side3)

    payload = {
        "data": bool(result),
    }

    return HttpResponse(json.dumps(payload), content_type="application/json")


def handle_task_04_palindrom(request: HttpRequest) -> HttpResponse:
    if request.GET:
        string = str(request.GET["q"])
        result = task_04_palindrom(string)

    payload = {
        "data": (result),
    }

    return HttpResponse(json.dumps(payload), content_type="application/json")
