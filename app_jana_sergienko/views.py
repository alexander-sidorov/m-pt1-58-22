from django.http import HttpResponse, HttpRequest


def helloworld(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello from app")
