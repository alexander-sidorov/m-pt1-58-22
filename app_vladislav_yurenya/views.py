from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render

from hw.vladislav_yurenya.lesson_04.lecture import task_01_money


def helloworld(request: HttpRequest) -> HttpResponse:
    return HttpResponse("HELLO FROM APP!")


def my_money(request: HttpRequest) -> HttpResponse:

    res: str = ""
    rubles: str | int = ""
    coins: str | int = ""
    amount: str | int = ""
    result = ""
    rubles = coins = amount = ""

    if request.GET:
        rubles = int(request.GET["r"])
        coins = int(request.GET["c"])
        amount = int(request.GET["a"])
        result = task_01_money(rubles, coins, amount)

    return render(
        request,
        "app_vladislav_yurenya/task01.html",
        {
            "r": rubles,
            "c": coins,
            "a": amount,
            "result": result,
        },
    )
