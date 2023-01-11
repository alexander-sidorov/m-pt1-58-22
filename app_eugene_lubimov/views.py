from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render
import json

import hw.eugene_lubimov.lesson04.lecture as les4


def helloworld(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello from app")


def handle_task_money(request: HttpRequest) -> HttpResponse:
    result: str | object = ""
    rubles = coins = amount = 0
    if request.GET:
        rubles, coins, amount = (
            int(request.GET["r"]),
            int(request.GET["c"]),
            int(request.GET["a"]),
        )
        result = les4.task_01_money(rubles, coins, amount)
    payload = {
        "data": float(result)
    }
    return HttpResponse(json.dumps(payload), content_type="application/json")

def handle_task_02_sign(request: HttpRequest) -> HttpResponse:
    result: int = 0
    if request.GET:
        number = request.GET["n"]
        result = les4.task_02_sign(number)

    payload = {
        "data": result
    }
    return HttpResponse(json.dumps(payload), content_type="application/json")
