import json
from decimal import Decimal

from django.http import HttpRequest
from django.http import HttpResponse

from hw.alexander_sidorov.lesson04.lecture import task_01_money


def helloworld(request: HttpRequest) -> HttpResponse:
    return HttpResponse("hello from app 12ewadsadsada")


def handle_task_01_money(request: HttpRequest) -> HttpResponse:
    result = Decimal()

    if request.GET:
        rubles = int(request.GET["r"])
        coins = int(request.GET["c"])
        amount = int(request.GET["a"])
        result = task_01_money(rubles, coins, amount)

    payload = {
        "data": float(result),
    }

    return HttpResponse(json.dumps(payload), content_type="application/json")
