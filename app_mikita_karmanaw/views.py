from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render


def hello_mk(request: HttpRequest) -> HttpResponse:
    response = render(
        request,
        "app_mikita_karmanaw/index_main.html",
        {"hello": "Welcome to Mikita Karmanaw's page!"},
    )
    return response


def money(request: HttpRequest) -> HttpResponse:
    from hw.mikita_karmanaw.lesson04.lecture import task_01_money

    res: str = ""
    rub: str | int = ""
    coins: str | int = ""
    amo: str | int = ""

    if request.GET:
        rub = int(request.GET["r"])
        coins = int(request.GET["c"])
        amo = int(request.GET["a"])
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
