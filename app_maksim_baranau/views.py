from django.http import HttpResponse, HttpRequest


def helloworld(request: HttpRequest) -> HttpResponse:
    return HttpResponse("hello from app ")