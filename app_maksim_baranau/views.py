from decimal import Decimal

from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render

from hw.maksim_baranau.lesson04.lecture import task_01_money


def helloworld(request: HttpRequest) -> HttpResponse:
    return HttpResponse("hello from APP")


def handle_task_01_money(request: HttpRequest) -> Decimal:
    dec_rubles = dec_coins = dec_amount = ""
    result = ""
    if request.GET:
        dec_rubles = Decimal(request.GET["r"])
        dec_coins = Decimal(request.GET["c"])
        dec_amount = Decimal(request.GET["a"])
        result = (dec_rubles + (dec_coins / 100)) * dec_amount

    return render(
        request, "app_maksim_baranau/task01.html", {"result": result}
    )
