from django.http import HttpRequest
from django.http import HttpResponse


def handle_sergey_sakovich(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Hello from Sergey Sakovich')
