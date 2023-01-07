from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render


def hello_mk(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello from mikitakarman's app!")


def money(request: HttpRequest) -> HttpResponse:
    from hw.mikita_karmanaw.lesson04.lecture import task_01_money

    res = ""
    rub: = coins = amo = ""

    if request.GET:
        rub = str(request.GET["r"])
        coins = str(request.GET["c"])
        amo = str(request.GET["a"])
        res = str(task_01_money(rub, coins, amo))
    html_out = render(
        request,
        "app_mikita_karmanaw/index_task_01.html",
        {
            "result": res,
            "r": rub,
            "c": coins,
            "a": amo,
        },
    )
    return HttpResponse(html_out)
