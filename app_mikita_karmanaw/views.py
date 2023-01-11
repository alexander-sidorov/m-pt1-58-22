import json

from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render


def hello_mk(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        "app_mikita_karmanaw/index_main.html"
    )


def money(request: HttpRequest) -> HttpResponse:
    from hw.mikita_karmanaw.lesson04.lecture import task_01_money

    res: str = ""
    rub: str | int = ""
    coins: str | int = ""
    amo: str | int = ""

    if not request.GET:
        html_out = render(
            request,
            "app_mikita_karmanaw/lesson04task01.html",
            {
                "r": rub,
                "c": coins,
                "a": amo,
            },
        )
        return HttpResponse(html_out)
    if request.GET:
        rub = int(request.GET["r"])
        coins = int(request.GET["c"])
        amo = int(request.GET["a"])
        res = str(task_01_money(rub, coins, amo))
    payload = {
        "data": {
            "result": res,
            "r": rub,
            "c": coins,
            "a": amo,
        },
    }
    return HttpResponse(json.dumps(payload), content_type="application/json")


def sign(request: HttpRequest) -> HttpResponse:
    from hw.mikita_karmanaw.lesson04.lecture import task_02_sign

    if not request.GET:
        html_out = render(request, "app_mikita_karmanaw/lesson04task02.html")
        return HttpResponse(html_out)
    else:
        num = int(request.GET["number"])
        res = str(task_02_sign(num))
        payload = {
            "data": {
                "number": num,
                "sign": res,
            },
        }
        return HttpResponse(
            json.dumps(payload), content_type="application/json"
        )


def triangle(request: HttpRequest) -> HttpResponse:
    from hw.mikita_karmanaw.lesson04.lecture import task_03_triangle

    if not request.GET:
        html_out = render(request, "app_mikita_karmanaw/lesson04task03.html")
        return HttpResponse(html_out)
    else:
        side1, side2, side3 = (
            int(request.GET["side1"]),
            int(request.GET["side2"]),
            int(request.GET["side3"]),
        )
        res = task_03_triangle(side1, side2, side3)
        payload = {
            "data": {
                "side1": side1,
                "side2": side2,
                "side3": side3,
                "triangle": res,
            },
        }
        return HttpResponse(
            json.dumps(payload), content_type="application/json"
        )


def palindrom(request: HttpRequest) -> HttpResponse:
    from hw.mikita_karmanaw.lesson04.lecture import task_04_palindrom

    if not request.GET:
        html_out = render(request, "app_mikita_karmanaw/lesson04task04.html")
        return HttpResponse(html_out)
    else:
        string = str(request.GET.get("str"))
        res = task_04_palindrom(string)
        payload = {
            "data": {
                "str": string,
                "palindrom": res,
            },
        }
        return HttpResponse(
            json.dumps(payload), content_type="application/json"
        )


def hdist(request: HttpRequest) -> HttpResponse:
    from hw.mikita_karmanaw.lesson06.tasks import task_03_hdist

    if not request.GET:
        html_out = render(request, "app_mikita_karmanaw/lesson06task03.html")
        return HttpResponse(html_out)
    else:
        seq1, seq2 = request.GET["seq1"], request.GET["seq2"]
        res = task_03_hdist(seq1, seq2)
        payload = {
            "data": {
                "seq1": seq1,
                "seq2": seq2,
                "hdist": res,
            },
        }
        return HttpResponse(
            json.dumps(payload), content_type="application/json"
        )


def cities(request: HttpRequest) -> HttpResponse:
    from hw.mikita_karmanaw.lesson06.tasks import CITIES
    from hw.mikita_karmanaw.lesson06.tasks import task_04_cities

    cities: list = []
    for city in CITIES:
        cities.append(city)

    if not request.GET:
        html_out = render(
            request,
            "app_mikita_karmanaw/lesson06task04.html",
            {"cities": cities},
        )
        return HttpResponse(html_out)
    else:
        city = request.GET["city"]
        res = task_04_cities(city)
        payload = {
            "data": {
                "city": city,
                "distances": res,
            },
        }
    return HttpResponse(json.dumps(payload), content_type="application/json")


def route(request: HttpRequest) -> HttpResponse:
    from hw.mikita_karmanaw.lesson06.tasks import CITIES
    from hw.mikita_karmanaw.lesson06.tasks import task_05_route

    cities: list = []
    for city in CITIES:
        cities.append(city)

    if not request.GET:
        html_out = render(
            request,
            "app_mikita_karmanaw/lesson06task05.html",
            {"cities": cities},
        )
        return HttpResponse(html_out)
    else:
        route = request.GET["route"]
        route_list = route.split(", ")
        res = task_05_route(route_list)
        payload = {
            "data": {
                "route": route,
                "distance": res,
            },
        }
        return HttpResponse(
            json.dumps(payload), content_type="application/json"
        )
