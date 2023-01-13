import json
from decimal import Decimal
from typing import Any

from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render

from hw.eugene_vavilov.lesson04.lecture import task_01_money
from hw.eugene_vavilov.lesson04.lecture import task_02_sign
from hw.eugene_vavilov.lesson04.lecture import task_03_triangle
from hw.eugene_vavilov.lesson04.lecture import task_04_palindrom
from hw.eugene_vavilov.lesson06.tasks import task_01_boundary
from hw.eugene_vavilov.lesson06.tasks import task_02_expand
from hw.eugene_vavilov.lesson06.tasks import task_03_hdist
from hw.eugene_vavilov.lesson06.tasks import task_04_cities
from hw.eugene_vavilov.lesson06.tasks import task_05_route


def helloworld(request: HttpRequest) -> HttpResponse:
    return HttpResponse("hello world 228")


def handle_task_01_money(request: HttpRequest) -> HttpResponse:
    rubles: int | str
    coins: int | str
    amount: int | str
    result: str | Decimal

    result = ""
    rubles = coins = amount = 0

    if request.GET:
        rubles = int(request.GET["r"])
        coins = int(request.GET["c"])
        amount = int(request.GET["a"])
        result = task_01_money(rubles, coins, amount)

        payload = {
            "data": float(result),
        }

        return HttpResponse(
            json.dumps(payload), content_type="application/json"
        )

    else:
        return render(
            request,
            "app_eugene_vavilov/lesson04_01.html",
            {
                "r": rubles,
                "c": coins,
                "a": amount,
                "result": result,
            },
        )


def handle_task_02_sign(request: HttpRequest) -> HttpResponse:
    number = 0
    result: str | int = ""

    if request.GET:
        number = int(request.GET["n"])
        result = task_02_sign(number)

        payload = {
            "data": int(result),
        }

        return HttpResponse(
            json.dumps(payload), content_type="application/json"
        )
    else:
        return render(
            request,
            "app_eugene_vavilov/lesson04_02.html",
            {
                "n": number,
                "result": result,
            },
        )


def handle_task_03_triangle(request: HttpRequest) -> HttpResponse:
    side1 = side2 = side3 = 0
    result: str | bool = ""
    if request.GET:
        side1 = int(request.GET["s1"])
        side2 = int(request.GET["s2"])
        side3 = int(request.GET["s3"])
        result = task_03_triangle(side1, side2, side3)

        payload = {
            "data": result,
        }

        return HttpResponse(
            json.dumps(payload), content_type="application/json"
        )
    else:
        return render(
            request,
            "app_eugene_vavilov/lesson04_03.html",
            {
                "s1": side1,
                "s2": side2,
                "s3": side3,
                "result": result,
            },
        )


def handle_task_04_palindrom(request: HttpRequest) -> HttpResponse:
    word = ""
    result: str | bool = ""
    if request.GET:
        word = request.GET["w"]
        result = task_04_palindrom(word)

        payload = {
            "data": result,
        }

        return HttpResponse(
            json.dumps(payload), content_type="application/json"
        )
    else:
        return render(
            request,
            "app_eugene_vavilov/lesson04_04.html",
            {
                "w": word,
                "result": result,
            },
        )


def handle_task_01_boudary(request: HttpRequest) -> HttpResponse:
    collect = ""
    result: tuple[Any, ...] = ()

    if request.GET:
        collect = request.GET["c"]
        result = task_01_boundary(collect)

        payload = {
            "data": result,
        }

        return HttpResponse(
            json.dumps(payload), content_type="application/json"
        )
    else:
        return render(
            request,
            "app_eugene_vavilov/lesson06_01.html",
            {
                "c": collect,
                "result": result,
            },
        )


def handle_task_02_expand(request: HttpRequest) -> HttpResponse:
    seq: list | str = ""
    result = ""

    if request.GET:
        seq = request.GET["s"]
        seq = seq.split(",")
        result = task_02_expand(seq)

        payload = {
            "data": result,
        }

        return HttpResponse(
            json.dumps(payload), content_type="application/json"
        )
    else:
        return render(
            request,
            "app_eugene_vavilov/lesson06_02.html",
            {
                "s": seq,
                "result": result,
            },
        )


def handle_task_03_hdist(request: HttpRequest) -> HttpResponse:
    seq1 = seq2 = ""
    result = 0

    if request.GET:
        seq1 = request.GET["s1"]
        seq2 = request.GET["s2"]
        result = task_03_hdist(seq1, seq2)

        payload = {
            "data": result,
        }

        return HttpResponse(
            json.dumps(payload), content_type="application/json"
        )
    else:
        return render(
            request,
            "app_eugene_vavilov/lesson06_03.html",
            {
                "s1": seq1,
                "s2": seq2,
                "result": result,
            },
        )


def handle_task_04_cities(request: HttpRequest) -> HttpResponse:
    town = ""
    result = {}

    if request.GET:
        town = request.GET["t"]
        result = task_04_cities(town)

        payload = {
            "data": result,
        }

        return HttpResponse(
            json.dumps(payload, ensure_ascii=False),
            content_type="application/json",
        )
    else:
        return render(
            request,
            "app_eugene_vavilov/lesson06_04.html",
            {
                "t": town,
                "result": result,
            },
        )


def handle_task_05_route(request: HttpRequest) -> HttpResponse:
    route: list[str] | str = []
    result = 0

    if request.GET:
        route = request.GET["r"]
        route = route.split(",")
        result = task_05_route(route)

        payload = {
            "data": result,
        }

        return HttpResponse(
            json.dumps(payload), content_type="application/json"
        )
    else:
        return render(
            request,
            "app_eugene_vavilov/lesson06_04.html",
            {
                "r": route,
                "result": result,
            },
        )
