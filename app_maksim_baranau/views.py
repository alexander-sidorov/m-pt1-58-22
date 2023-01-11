import json
from decimal import Decimal
from typing import Any

from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render

from hw.maksim_baranau.lesson04.lecture import task_01_money, task_02_sign, task_03_triangle, task_04_palindrom


def helloworld(request: HttpRequest) -> HttpResponse:
    return HttpResponse("hello from APP")


def handle_task_01_money(request: HttpRequest) -> HttpResponse:
    result = Decimal(0)
    if request.GET:
        dec_rubles = int(request.GET["r"])
        dec_coins = int(request.GET["c"])
        dec_amount = int(request.GET["a"])
        result = task_01_money(dec_rubles, dec_coins, dec_amount)

    return render(
        request, "app_maksim_baranau/task01.html", {"result": result}
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
        result = task_03_triangle(side1, side2, side3
                                  )
    payload = {
        "data": bool(result),
    }
    return HttpResponse(json.dumps(payload), content_type="application/json")


def handle_task_04_palindrom(request: HttpRequest) -> HttpResponse:
    if request.GET:
        text = str(request.GET["t"])
        result = task_04_palindrom(text)
    payload = {
        "data": bool(result),
    }
    return HttpResponse(json.dumps(payload), content_type="application/json")