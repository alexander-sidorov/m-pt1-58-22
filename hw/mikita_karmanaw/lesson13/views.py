from django.http import HttpRequest
from django.http import HttpResponse


def handle_mikita_karmanaw(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello from Mikita Karmanaw")
