from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

from hw.dmitry_mihkailiuk.lesson04.lecture import task_01_money


def helloworld(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello from app!")


def handle_task_01_money(request: HttpRequest) -> HttpResponse:
    result = ""
    rub = coins = amount = ""

    if request.GET:
        rub = int(request.GET['r'])
        coins = int(request.GET['c'])
        amount = int(request.GET['a'])
        result = task_01_money(rub, coins, amount)

    return render(
        request,
        "app_dmitry_mikhailiuk/task01.html",
        {
            "r": rub,
            "c": coins,
            "a": amount,
            "result": result,
        },
    )
