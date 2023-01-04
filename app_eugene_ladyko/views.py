from django.http import HttpResponse
from django.http import HttpRequest


def helloworld(request: HttpRequest) -> HttpResponse:
    return HttpResponse("hello from app ")
