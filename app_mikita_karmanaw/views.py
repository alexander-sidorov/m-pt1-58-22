from django.http import HttpRequest
from django.http import HttpResponse


def hello_mk(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello from mikitakarman's app!")


def money(request: HttpRequest) -> HttpResponse:
    from hw.mikita_karmanaw.lesson04.lecture import task_01_money

    rub = int(request.GET["r"])
    coins = int(request.GET["c"])
    amo = int(request.GET["a"])
    res = task_01_money(rub, coins, amo)
    return HttpResponse(res)
