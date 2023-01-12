import json
from decimal import Decimal
from typing import Any

from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render

import hw.vadim_zharski.lesson06.tasks as les6
import hw.vadim_zharski.lesson_04.lecture as les4


def hello_world_vadim_zharski(request: HttpRequest) -> HttpResponse:
    helloworld: str = "hello from Vadim Zharski app"
    content: dict = {"hello": helloworld}
    return render(request, "app_vadim_zharski/index.html", content)


def task_money(request: HttpRequest) -> HttpResponse:
    if request.GET:
        rubles = int(request.GET["rubles"])
        coins = int(request.GET["coins"])
        amount = int(request.GET["amount"])
        result = float(les4.task_01_money(rubles, coins, amount))
        content: dict = {
            "data": {
                "rubles": rubles,
                "coins": coins,
                "amount": amount,
                "result": result,
            }}
        if 'html' in request.GET:
            return render(request, "app_vadim_zharski/task_01.html", content)
        if 'json' in request.GET:
            return HttpResponse(json.dumps(content), content_type="application/json")
    return render(request, "app_vadim_zharski/task_01.html")


def task_sign(request: HttpRequest) -> HttpResponse:
    if request.GET:
        num = float(request.GET["num"])
        result = les4.task_02_sign(num)
        content: dict = {
            "data": {
                "num": num,
                "result": result,
            }}
        if 'html' in request.GET:
            return render(request, "app_vadim_zharski/task_02.html", content)
        if 'json' in request.GET:
            return HttpResponse(json.dumps(content), content_type="application/json")
    return render(request, "app_vadim_zharski/task_02.html")


def task_triangle(request: HttpRequest) -> HttpResponse:
    if request.GET:
        side1 = float(request.GET["side1"])
        side2 = float(request.GET["side2"])
        side3 = float(request.GET["side3"])
        result = les4.task_03_triangle(side1, side2, side3)
        content: dict = {
            "data": {
                "side1": side1,
                "side2": side2,
                "side3": side3,
                "result": result,
            }}
        if 'html' in request.GET:
            return render(request, "app_vadim_zharski/task_03.html", content)
        if 'json' in request.GET:
            return HttpResponse(json.dumps(content), content_type="application/json")
    return render(request, "app_vadim_zharski/task_03.html")


def task_palindrom(request: HttpRequest) -> HttpResponse:
    if request.GET:
        string = str(request.GET["string"])
        result = les4.task_04_palindrom(string)
        content: dict = {
            "data": {
                "string": string,
                "result": result,
            }}
        if 'html' in request.GET:
            return render(request, "app_vadim_zharski/task_04.html", content)
        if 'json' in request.GET:
            return HttpResponse(json.dumps(content), content_type="application/json")
    return render(request, "app_vadim_zharski/task_04.html")


def task_06_boundary(request: HttpRequest) -> HttpResponse:
    if request.GET:
        arr = str(request.GET["arr"])
        result = les6.task_01_boundary(arr)
        content: dict = {
            "data": {
                "arr": arr,
                "result": result,
            }}
        if 'html' in request.GET:
            return render(request, "app_vadim_zharski/task_06_01.html", content)
        if 'json' in request.GET:
            return HttpResponse(json.dumps(content), content_type="application/json")
    return render(request, "app_vadim_zharski/task_06_01.html")
