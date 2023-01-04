from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render

from hw.jana_sergienko.lesson04.lecture import task_01_money


def helloworld(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello from app")


def handle_task_01_money(request: HttpRequest) -> HttpResponse:
    result = ""
    rub = coin = amt = ""

    if request.GET:
        rub = int(request.GET["r"])
        coin = int(request.GET["c"])
        amt = int(request.GET["a"])
        result = task_01_money(rub, coin, amt)

    return render(
        request,
        "app_jana_sergienko/task01.html",
        {
            "r": rub,
            "c": coin,
            "a": amt,
            "result": result,
        },
    )
