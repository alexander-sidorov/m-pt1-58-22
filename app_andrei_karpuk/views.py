from django.http import HttpRequest
from django.http import HttpResponse
from hw.andrei_karpuk.lesson04.lecture import task_01_money
from django.shortcuts import render

def helloworld_ak(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello from App")



def task_money(request: HttpRequest) -> HttpResponse:
    result = ""
    rubles = coin = amount = ""

    if request.GET:
        rubles = int(request.GET["r"])
        coin = int(request.GET["c"])
        amount = int(request.GET["a"])
        result = task_01_money(rubles, coin, amount)

    return render(
        request,
        "app_andrei_karpuk/task01.html",
        {
            "r": rubles,
            "c": coin,
            "a": amount,
            "result": result,
        },
    )
