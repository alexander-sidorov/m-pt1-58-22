import json

from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render

import hw.eugene_lubimov.lesson04.lecture as les4
import hw.eugene_lubimov.lesson06.tasks as les6


def helloworld(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello from app")


def handle_task_money(request: HttpRequest) -> HttpResponse:
    if not request.GET:
        return render(request, "app_eugene_lubimov/task01.html")

    rubles = int(request.GET["r"])
    coins = int(request.GET["c"])
    amount = int(request.GET["a"])
    result = les4.task_01_money(rubles, coins, amount)

    payload = {
        "data": float(result),
    }

    return HttpResponse(json.dumps(payload), content_type="application/json")


def handle_task_02_sign(request: HttpRequest) -> HttpResponse:
    if not request.GET:
        return render(request, "app_eugene_lubimov/task02.html")

    number = int(request.GET["n"])
    result = les4.task_02_sign(number)
    payload = {
        "data": int(result),
    }
    return HttpResponse(json.dumps(payload), content_type="application/json")


def handle_task_03_triangle(request: HttpRequest) -> HttpResponse:
    if not request.GET:
        return render(request, "app_eugene_lubimov/task03.html")

    side1, side2, side3 = (
        int(request.GET["s1"]),
        int(request.GET["s2"]),
        int(request.GET["s3"]),
    )
    result = les4.task_03_triangle(side1, side2, side3)
    payload = {
        "data": bool(result),
    }
    return HttpResponse(json.dumps(payload), content_type="application/json")


def handle_task_04_palindrom(request: HttpRequest) -> HttpResponse:
    if not request.GET:
        return render(request, "app_eugene_lubimov/task04.html")
    string = request.GET["s"]
    result = les4.task_04_palindrom(string)
    payload = {
        "data": bool(result),
    }
    return HttpResponse(json.dumps(payload), content_type="application/json")


def handle_task_01_boundary(request: HttpRequest) -> HttpResponse:
    if not request.GET:
        return render(request, "app_eugene_lubimov/task05.html")
    seq = request.GET["s"][1:-1].split(", ")
    result = les6.task_01_boundary(seq)
    payload = {
        "data": list(result),
    }
    return HttpResponse(json.dumps(payload), content_type="application/json")


def handle_task_02_expand(request: HttpRequest) -> HttpResponse:
    if not request.GET:
        return render(request, "app_eugene_lubimov/task06.html")
    seq = request.GET["s"][1:-1].split(", ")
    result = les6.task_02_expand(seq)
    payload = {
        "data": list(result),
    }
    return HttpResponse(json.dumps(payload), content_type="application/json")


def handle_task_03_hdist(request: HttpRequest) -> HttpResponse:
    if not request.GET:
        return HttpResponse(" ")
    seq1, seq2 = request.GET["s1"][1:-1].split(", "), request.GET["s1"][
        1:-1
    ].split(", ")
    result = les6.task_03_hdist(seq1, seq2)
    payload = {
        "data": int(result),
    }
    return HttpResponse(json.dumps(payload), content_type="application/json")
