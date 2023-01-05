from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render

from hw.vadim_zharski.lesson_04.lecture import task_01_money


def hello_world_vadim_zharski(request: HttpRequest) -> HttpResponse:
    helloworld: str = "hello from Vadim Zharski app"
    content: dict = {"hello": helloworld}
    return render(request, "app_vadim_zharski/index.html", content)


def task_money(request: HttpRequest) -> HttpResponse:
    result = ""
    rubles = coins = amount = ""

    if request.GET:
        rubles = int(request.GET["r"])
        coins = int(request.GET["c"])
        amount = int(request.GET["a"])
        result = task_01_money(rubles, coins, amount)
    res: dict = {
        "r": rubles,
        "c": coins,
        "a": amount,
        "result": result,
    }
    return render(request, "app_vadim_zharski/task_01.html", res)
