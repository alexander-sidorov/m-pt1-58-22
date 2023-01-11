import json
from decimal import Decimal

from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render

from hw.vadim_zharski.lesson_04.lecture import task_01_money


def hello_world_vadim_zharski(request: HttpRequest) -> HttpResponse:
    helloworld: str = "hello from Vadim Zharski app"
    content: dict = {"hello": helloworld}
    return render(request, "app_vadim_zharski/index.html", content)


def task_money(request: HttpRequest) -> HttpResponse:
    result: str | Decimal = ""
    rubles: str | int = ""
    coins: str | int = ""
    amount: str | int = ""
    res: dict = {
        "r": rubles,
        "c": coins,
        "a": amount,
        "result": result,
    }
    if not request.GET:
        return render(request, "app_vadim_zharski/task_01.html", res)

    rubles = int(request.GET["r"])
    coins = int(request.GET["c"])
    amount = int(request.GET["a"])
    result = task_01_money(rubles, coins, amount)
    payload = {
        "rubles": rubles,
        "coins": coins,
        "amount": amount,
        "data": float(result),
    }
    return HttpResponse(json.dumps(payload), content_type="application/json")

