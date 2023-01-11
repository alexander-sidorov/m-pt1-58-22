import json
from decimal import Decimal

from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render

from hw.eugene_vavilov.lesson04.lecture import task_01_money
from hw.eugene_vavilov.lesson04.lecture import task_02_sign


def helloworld(request: HttpRequest) -> HttpResponse:
    return HttpResponse("hello world 228")


def handle_task_01_money(request: HttpRequest) -> HttpResponse:
    rubles: int | str
    coins: int | str
    amount: int | str
    result: str | Decimal

    result = ""
    rubles = coins = amount = 0

    if request.GET:
        rubles = int(request.GET["r"])
        coins = int(request.GET["c"])
        amount = int(request.GET["a"])
        result = task_01_money(rubles, coins, amount)
    else:
        return render(
            request,
            "app_alexander_sidorov/task01.html",
            {
                "r": rubles,
                "c": coins,
                "a": amount,
                "result": result,
            },
        )

    payload = {
        "data": int(result),
    }

    return HttpResponse(json.dumps(payload), content_type="application/json")


def handle_task_02_sign(request: HttpRequest) -> HttpResponse:
    if request.GET:
        number = int(request.GET["n"])
        result = task_02_sign(number)

    payload = {
        "data": float(result),
    }

    return HttpResponse(json.dumps(payload), content_type="application/json")
