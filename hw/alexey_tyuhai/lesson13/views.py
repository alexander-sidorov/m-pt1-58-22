from django.http import HttpRequest
from django.http import HttpResponse


def handle_alexey_tuyhai(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello from Alexey Tuyhai")
