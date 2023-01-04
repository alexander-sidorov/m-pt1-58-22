from django.http import HttpRequest
from django.http import HttpResponse


def handle_dmitry_mikhailiuk(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello from Dmitry Mikhailiuk")
