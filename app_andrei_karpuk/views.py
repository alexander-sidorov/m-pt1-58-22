from decimal import Decimal
import json
from typing import Any

from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render

from hw.andrei_karpuk.lesson04.lecture import task_01_money, task_02_sign, task_03_triangle, task_04_palindrom


def helloworld_ak(request: HttpRequest) -> HttpResponse:
    if request:
        return render(request)
    return HttpResponse("Hello from App")


def task_money(request: HttpRequest) -> HttpResponse:

    if not request.GET:
        return render(request, "app_andrei_karpuk/task01.html")

    rubles = int(request.GET["r"])
    coin = int(request.GET["c"])
    amount = int(request.GET["a"])
    result = task_01_money(rubles, coin, amount)

    payload = {
        "data": float(result),
    }

    return HttpResponse(json.dumps(payload), content_type="application/json")

def task_sign(request: HttpRequest) -> HttpResponse:

        if not request.GET:
            return render(request, "app_andrei_karpuk/task02.html")
        number = (request.GET["n"])
        result = task_02_sign(number)
        payload = {
            "data": result
        }

        return HttpResponse(json.dumps(payload), content_type="application/json")


    #return render(
        #request,
        #"app_andrei_karpuk/task01.html",
        #{
           # "r": rubles,
          #  "c": coin,
           # "a": amount,
          #  "result": result,
       # },
    #)
