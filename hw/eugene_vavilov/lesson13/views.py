from django.http import HttpRequest
from django.http import HttpResponse


def handle_eugene_vavilov(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello world")
