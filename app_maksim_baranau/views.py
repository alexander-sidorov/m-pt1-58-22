from decimal import Decimal

from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render

from hw.maksim_baranau.lesson04.lecture import task_01_money


def helloworld(request: HttpRequest) -> HttpResponse:
    return HttpResponse("hello from APP")


def handle_task_01_money(request: HttpRequest) -> HttpResponse:
    dec_rubles = dec_coins = dec_amount = 0
    result = Decimal(0)
    if request.GET:
        dec_rubles = int(request.GET["r"])
        dec_coins = int(request.GET["c"])
        dec_amount = int(request.GET["a"])
        result = task_01_money(dec_rubles, dec_coins, dec_amount)

    return render(
        request, "app_maksim_baranau/task01.html", {"result": result}
    )
