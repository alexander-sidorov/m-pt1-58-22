from django.http import HttpRequest
from django.http import HttpResponse


def hello_mk(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello from mikitakarman's app!")


html = """
<html>
<head></head>
<body>
<form action="/~/mikita_karmanaw/lesson04/task01/" method="get">

Rubles: <input type="text" name="r">
Coins: <input type="text" name="c">
Amount: <input type="text" name="a">

<button type="submit">Calculate</button>

<h3>{result}</h3>

</form>
</body>
</html>
"""


def money(request: HttpRequest) -> HttpResponse:
    from hw.mikita_karmanaw.lesson04.lecture import task_01_money

    res = ""

    if request.GET:
        rub = int(request.GET["r"])
        coins = int(request.GET["c"])
        amo = int(request.GET["a"])
        res = task_01_money(rub, coins, amo)
    html_out = html.format(result=res)
    return HttpResponse(html_out)
