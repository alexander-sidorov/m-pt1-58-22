import json

from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render

from hw.dmitry_mihkailiuk.lesson04.lecture import task_01_money
from hw.dmitry_mihkailiuk.lesson04.lecture import task_02_sign
from hw.dmitry_mihkailiuk.lesson04.lecture import task_03_triangle
from hw.dmitry_mihkailiuk.lesson04.lecture import task_04_palindrom
from hw.dmitry_mihkailiuk.lesson06.tasks import task_01_boundary


def helloworld(request: HttpRequest) -> HttpResponse:
    return render(request, "app_dmitry_mikhailiuk/index.html")


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


def handle_task_02_sign(request: HttpRequest) -> HttpResponse:
    if request.GET:
        number = int(request.GET["n"])
        result = task_02_sign(number)

        payload = {
            "data": result,
        }

        return HttpResponse(json.dumps(payload), content_type="application/json")

    return render(request, "app_dmitry_mikhailiuk/task02.html")


def handle_task_03_triangle(request: HttpRequest) -> HttpResponse:
    if request.GET:
        side1 = float(request.GET["s1"])
        side2 = float(request.GET["s2"])
        side3 = float(request.GET["s3"])
        result = task_03_triangle(side1, side2, side3)

        payload = {
            "data": result,
        }

        return HttpResponse(json.dumps(payload), content_type="application/json")


def handle_task_04_palindrom(request: HttpRequest) -> HttpResponse:
    if request.GET:
        st = request.GET["s"]
        result = task_04_palindrom(st)

        payload = {
            "data": result,
        }

        return HttpResponse(json.dumps(payload), content_type="application/json")


def handle_task_01_boundary(request: HttpRequest) -> HttpResponse:
    if request.GET:
        tup = tuple(request.GET["s"])
        first, last = task_01_boundary(tup)

        payload = {
            "data": {
                "original": request.GET["s"],
                "first": first,
                "last": last
            }
        }

        return HttpResponse(json.dumps(payload), content_type="application/json")