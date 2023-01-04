from django.http import HttpRequest
from django.http import HttpResponse


def ak_view(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello from Andrei Karpuk")