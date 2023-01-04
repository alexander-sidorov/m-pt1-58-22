from django.http import HttpResponse,HttpRequest
from hw.sergey_sakovich.lesson04.lecture import task_01_money


def helloworld(request: HttpRequest) -> HttpResponse:
    return HttpResponse('HELLO FROM APP!')

HTML = """
<html>
<head>
</head>
<body>

<form action="/~/sergey_sakovich/l04/t1/" method="get">

Rubles: <input type="text" name="r">
Coins: <input type="text" name="c">
Amount: <input type="text" name="a">

<button type="submit">Calculate</button>
</form>

<h1>{result}</h1>

</body>
</html>
"""


def task_money(request: HttpRequest) -> HttpResponse:
    result = ""
    if request.Get:
        r = int(request.GET['r'])
        c = int(request.GET['c'])
        a = int(request.GET['a'])
        result = task_01_money(r, c, a)

    return render(
        request,
        "app_alexander_sidorov/task01.html",
        {
            "r": rubles,
            "c": coins,
            "a": amount,
            "result": result,
        },
    )
