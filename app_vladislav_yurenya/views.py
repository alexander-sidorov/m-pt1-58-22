import json
from decimal import Decimal

from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render

from hw.vladislav_yurenya.lesson06.tasks import task_01_boundary
from hw.vladislav_yurenya.lesson_04.lecture import task_01_money
from hw.vladislav_yurenya.lesson_04.lecture import task_02_sign
from hw.vladislav_yurenya.lesson_04.lecture import task_03_triangle
from hw.vladislav_yurenya.lesson_04.lecture import task_04_palindrom


def helloworld(request: HttpRequest) -> HttpResponse:
    return render(
        request, "app_vladislav_yurenya/hello.html", {"hello": "HELLO WORLD"}
    )


def my_money(request: HttpRequest) -> HttpResponse:
    result = Decimal()
    rubles: str | int = ""
    coins: str | int = ""
    amount: str | int = ""

    if not request.GET:
        return render(request, "app_vladislav_yurenya/task01.html")
    rubles = int(request.GET["r"])
    coins = int(request.GET["c"])
    amount = int(request.GET["a"])
    result = task_01_money(rubles, coins, amount)
    payload = {"data": float(result)}
    return HttpResponse(json.dumps(payload), content_type="application/json")


def sign(request: HttpRequest) -> HttpResponse:
    number: str | float = ""
    res: float | str = ""
    if not request.GET:
        return render(request, "app_vladislav_yurenya/task02.html")
    number = float(request.GET["number"])
    res = task_02_sign(number)
    payloads = {"data": res}
    return HttpResponse(json.dumps(payloads), content_type="application/json")


def triangle(request: HttpRequest) -> HttpResponse:
    result = bool()
    side1: str | float = ""
    side2: str | float = ""
    side3: str | float = ""
    if not request.GET:
        return render(request, "app_vladislav_yurenya/task03.html")
    side1 = float(request.GET["s1"])
    side2 = float(request.GET["s2"])
    side3 = float(request.GET["s3"])
    result = task_03_triangle(side1, side2, side3)
    payloads = {"data": bool(result)}
    return HttpResponse(json.dumps(payloads), content_type="application/json")


def palindrom(request: HttpRequest) -> HttpResponse:
    string: str = ""
    if not request.GET:
        return render(request, "app_vladislav_yurenya/task04.html")

    string = str(request.GET["string"])
    result = task_04_palindrom(string)
    payloads = {"data": bool(result)}
    return HttpResponse(json.dumps(payloads), content_type="application/json")


def boundary(request: HttpRequest) -> HttpResponse:
    seq: str = ""
    res: tuple
    if not request.GET:
        return render(request, "app_vladislav_yurenya/task_6_01.html")
    seq = str(request.GET["seq"])
    result = task_01_boundary(seq)
    payloads = {"data": result}
    return HttpResponse(json.dumps(payloads), content_type="application/json")
