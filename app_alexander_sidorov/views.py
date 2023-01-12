from typing import Callable

from django.http import HttpRequest
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render

from hw.alexander_sidorov.lesson04 import lecture as lesson04


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "app_alexander_sidorov/index.html")


def api(handler: Callable) -> Callable:
    def wrapped(*args: tuple, **kwargs: dict) -> HttpResponse:
        try:
            data = handler(*args, **kwargs)
            return JsonResponse({"data": data})
        except Exception as err:
            import traceback

            return JsonResponse(
                {
                    "errors": [str(err)],
                    "tb": traceback.format_exc(),
                }
            )

    return wrapped


@api
def handle_04_01_money(request: HttpRequest) -> float:
    assert request.GET, "cannot calculate without args"

    rubles = int(request.GET["r"])
    coins = int(request.GET["c"])
    amount = int(request.GET["a"])

    return float(lesson04.task_01_money(rubles, coins, amount))


@api
def handle_04_02_sign(request: HttpRequest) -> int:
    assert request.GET, "cannot calculate without args"

    number = float(request.GET["n"])

    return lesson04.task_02_sign(number)


@api
def handle_04_03_triangle(request: HttpRequest) -> bool:
    assert request.GET, "cannot calculate without args"

    sides: list[int] = [int(request.GET[s]) for s in "abc"]

    return lesson04.task_03_triangle(*sides)


@api
def handle_04_04_palindrome(request: HttpRequest) -> bool:
    assert request.GET, "cannot calculate without args"

    text = request.GET["t"]

    return lesson04.task_04_palindrom(text)
