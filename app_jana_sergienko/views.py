import json

from django.http import HttpRequest
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render

from hw.jana_sergienko.lesson04.lecture import task_01_money
from hw.jana_sergienko.lesson04.lecture import task_02_sign
from hw.jana_sergienko.lesson04.lecture import task_03_triangle
from hw.jana_sergienko.lesson04.lecture import task_04_palindrom


def helloworld(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello from app")


def handle_task_01_money(request: HttpRequest) -> HttpResponse:
    if not request.GET:
        return render(request, "app_jana_sergienko/task01.html")

    rub = int(request.GET["r"])
    coin = int(request.GET["c"])
    amt = int(request.GET["a"])
    result = task_01_money(rub, coin, amt)

    payload = {
        "data": {
            "rubles": rub,
            "coins": coin,
            "amount": amt,
            "result": float(result),
        }
    }

    return JsonResponse(payload)


def handle_task_02_sign(request: HttpRequest) -> HttpResponse:
    result = 0
    if request.GET:
        number = float(request.GET["n"])
        result = task_02_sign(number)

    payload = {
        "data": {
            "number": number,
            "result": result,
        }
    }

    return JsonResponse(payload)


def handle_task_03_triangle(request: HttpRequest) -> HttpResponse:
    if request.GET:
        side1 = int(request.GET["s1"])
        side2 = int(request.GET["s2"])
        side3 = int(request.GET["s3"])
        result = task_03_triangle(side1, side2, side3)

    payload = {
        "data": {
            "side1": side1,
            "side2": side2,
            "side3": side3,
            "triangle": result,
        }
    }

    return JsonResponse(payload)


def handle_task_04_palindrom(request: HttpRequest) -> HttpResponse:
    str_ = ""
    result = False
    if request.GET:
        str_ = request.GET["str"]
        result = task_04_palindrom(str_)

    payload = {
        "data": {
            "line": str_,
            "result": result,
        }
    }

    return JsonResponse(payload)
