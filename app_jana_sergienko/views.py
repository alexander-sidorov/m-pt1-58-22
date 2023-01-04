from django.http import HttpRequest
from django.http import HttpResponse

from hw.jana_sergienko.lesson04.lecture import task_01_money


def helloworld(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello from app")


def handle_task_01_money(request: HttpRequest) -> HttpResponse:
    rub = int(request.GET["r"])
    coin = int(request.GET["c"])
    amt = int(request.GET["a"])
    res = task_01_money(rub, coin, amt)
    return HttpResponse(res, content_type="text/plain")
