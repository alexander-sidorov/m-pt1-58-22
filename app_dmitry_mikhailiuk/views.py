import json

from django.http import HttpRequest
from django.http import HttpResponse

from django.shortcuts import render

from hw.dmitry_mihkailiuk.lesson04.lecture import task_01_money


def helloworld(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello from app!")


def handle_task_01_money(request: HttpRequest) -> HttpResponse:
    if not request.GET:
        return render(request, "app_dmitry_mikhailiuk/task01.html")

    rubles = int(request.GET["r"])
    coins = int(request.GET["c"])
    amount = int(request.GET["a"])
    result = task_01_money(rubles, coins, amount)

    payload = {
        "data": float(result),
    }

    return HttpResponse(json.dumps(payload), content_type="application/json")
