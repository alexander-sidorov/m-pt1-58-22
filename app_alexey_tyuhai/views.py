from decimal import Decimal

from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render

from hw.alexey_tyuhai.lesson04.lecture import task_01_money


def hello(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello from app_alexey_tyuhai")


def handle_task_01_money(request: HttpRequest) -> HttpResponse:
    rubles: str | int = ""
    coins: str | int = ""
    amount: str | int = ""
    result: str | Decimal = ""

    if request.GET:
        rubles = int(request.GET["r"])
        coins = int(request.GET["c"])
        amount = int(request.GET["a"])
        result = task_01_money(rubles, coins, amount)

    return render(
        request,
        "app_alexey_tyuhai/task01.html",
        {"result": result, "r": rubles, "c": coins, "a": amount},
    )
