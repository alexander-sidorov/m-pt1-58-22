import json

from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render

from hw.maksim_lamaka.lesson04.lecture import task_01_money
from hw.maksim_lamaka.lesson04.lecture import task_03_triangle
from hw.maksim_lamaka.lesson04.lecture import task_04_palindrom


def helloworld(request: HttpRequest) -> HttpResponse:
    return HttpResponse("hello from app")


HTML = """

"""


def task_money(request: HttpRequest) -> HttpResponse:
    result = ""
    rubles = coins = amount = ""

    if request.GET:
        rubles = int(request.GET["r"])
        coins = int(request.GET["c"])
        amount = int(request.GET["a"])
        result = task_01_money(rubles, coins, amount)

    return render(
        request,
        "app_maksim_lamaka/task01.html",
        {
            "r": rubles,
            "c": coins,
            "a": amount,
            "result": result,
        },
    )


def task_palindrom(request: HttpRequest) -> HttpResponse:
    if request.GET:
        string = str(request.GET["t"])
        result = task_04_palindrom(string)

    payload = {"data": bool(result)}
    return HttpResponse(json.dumps(payload), content_type="application/json")


def task_triangle(request: HttpRequest) -> HttpResponse:
    if request.GET:
        side1 = float(request.GET["a"])
        side2 = float(request.GET["b"])
        side3 = float(request.GET["c"])
        result = task_03_triangle(side1, side2, side3)

    payload = {"data": bool(result)}
    return HttpResponse(json.dumps(payload), content_type="application/json")
