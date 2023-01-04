from django.http import HttpRequest
from django.http import HttpResponse

from hw.jana_sergienko.lesson04.lecture import task_01_money


def helloworld(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello from app")


HTML = """
<html>
<head>
</head>
<body>
<form action="/~/jana_sergienko/lesson04/task01/" method="get">
Rubles: <input type="text" name="r">
Coins: <input type="text" name="c">
Amount: <input type="text" name="a">
<button type="submit">Calculate</button>
</form>
<h1>{result}</h1>
</body>
</html>
"""


def handle_task_01_money(request: HttpRequest) -> HttpResponse:
    result = ""

    if request.GET:
        rub = int(request.GET["r"])
        coin = int(request.GET["c"])
        amt = int(request.GET["a"])
        result = task_01_money(rub, coin, amt)

    html = HTML.format(result=result)

    return HttpResponse(html)
