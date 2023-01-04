from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render

from hw.alexander_sidorov.lesson04.lecture import task_01_money


def helloworld(request: HttpRequest) -> HttpResponse:
    return HttpResponse("hello from app 12ewadsadsada")


def handle_task_01_money(request: HttpRequest) -> HttpResponse:
    result = ""
    rubles = coins = amount = ""

    if request.GET:
        rubles = int(request.GET["r"])
        coins = int(request.GET["c"])
        amount = int(request.GET["a"])
        result = task_01_money(rubles, coins, amount)

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
