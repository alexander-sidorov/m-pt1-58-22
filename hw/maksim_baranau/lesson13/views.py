from django.http import HttpRequest
from django.http import HttpResponse


def handle_maksim_baranau(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello from Maksim Baranau")
