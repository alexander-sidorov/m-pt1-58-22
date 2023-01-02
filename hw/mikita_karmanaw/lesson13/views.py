from django.http import HttpResponse
from django.http import HttpRequest


def handle_mikita_karmanaw(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello from Mikita Karmanaw")
