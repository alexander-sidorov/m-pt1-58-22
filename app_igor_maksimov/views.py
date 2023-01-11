from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render
import json

from hw.alexander_sidorov.lesson04.lecture import task_01_money, task_02_sign,task_03_triangle


def helloworld(request: HttpRequest) -> HttpResponse:
    if request:
        return render(request, 'app_igor_maksimov/main.html')
    else:
        return HttpResponse('Hello world')

def handle_task_01_money(request: HttpRequest) -> HttpResponse:
   
    if not request.GET:
        return render(request, 'app_igor_maksimov/task01.html')

    rubles = int(request.GET["r"])
    coins = int(request.GET["c"])
    amount = int(request.GET["a"])
    result = task_01_money(rubles, coins, amount)

    payload = {
        'data': float(result) 
    }
    return HttpResponse(json.dumps(payload), content_type= "application/json")
 

def handle_task_02_sign(request: HttpRequest)-> HttpResponse:
   if not request.GET:
       return render(request, 'app_igor_maksimov/task04_02.html')
       
   number = int(request.GET['x'])
   result = task_02_sign(number)
   payload = {
       'data': result
   }
   return HttpResponse(json.dumps(payload), content_type= "application/json")

def handle_task_triagle(request:HttpRequest)-> HttpResponse:
    if not request.GET:
        return render(request, 'app_igor_maksimov/task04_03.html')
    side1= request.GET['a']
    side2= request.GET['b']
    side3= request.GET['c']
    result = task_03_triangle(side1,side2,side3)

    payload = {
        'data': result
    }
    return HttpResponse(json.dumps(payload), content_type= "application/json")