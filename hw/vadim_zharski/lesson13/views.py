from django.http import HttpRequest
from django.http import HttpResponse


def handle_vadim_zharski(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello from Vadim Zharkski")
