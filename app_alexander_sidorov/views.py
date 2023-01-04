from django.http import HttpRequest
from django.http import HttpResponse

from hw.alexander_sidorov.lesson04.lecture import task_01_money


def helloworld(request: HttpRequest) -> HttpResponse:
    return HttpResponse("hello from app 12ewadsadsada")


HTML = """
<html>
<head>
</head>
<body>

<form action="/~/alexander_sidorov/lesson04/task01/" method="get">

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
        rubles = int(request.GET["r"])
        coins = int(request.GET["c"])
        amount = int(request.GET["a"])
        result = task_01_money(rubles, coins, amount)

    html = HTML.format(result=result)

    return HttpResponse(html)
