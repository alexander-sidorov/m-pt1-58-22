from decimal import Decimal

from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render

from hw.eugene_vavilov.lesson04.lecture import task_01_money


def helloworld(request: HttpRequest) -> HttpResponse:
    return HttpResponse("hello world 228")


def handle_task_01_money(request: HttpRequest) -> HttpResponse:
    rubles: int | str
    coins: int | str
    amount: int | str
    result: str | Decimal

    result = ""
    rubles = coins = amount = ""

    if request.GET:
        rubles = int(request.GET["r"])
        coins = int(request.GET["c"])
        amount = int(request.GET["a"])
        result = task_01_money(rubles, coins, amount)

    return render(
        request,
        "app_eugene_vavilov/lesson04.html",
        {
            "r": rubles,
            "c": coins,
            "a": amount,
            "result": result,
        },
    )
