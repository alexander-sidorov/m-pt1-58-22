from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render

from hw.eugene_lubimov.lesson04.lecture import task_01_money


def helloworld(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello from app")


def handle_task_money(request: HttpRequest) -> HttpResponse:
    result = ""
    rubles = coins = amount = ""
    if request.GET:
        rubles, coins, amount = (
            int(request.GET["r"]),
            int(request.GET["c"]),
            int(request.GET["a"]),
        )
        result = task_01_money(rubles, coins, amount)

    return render(
        request,
        "app_eugene_lubimov/task01.html",
        {
            "r": rubles,
            "c": coins,
            "a": amount,
            "result": result,
        },
    )
