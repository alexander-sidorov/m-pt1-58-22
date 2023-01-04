from django.http import HttpResponse, HttpRequest


def helloworld(request: HttpResponse) -> HttpResponse:
    return HttpResponse("hello from app")
