from django.http import HttpRequest
from django.http import HttpResponse


def hello_world_vadim_zharski(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello from app (vadim_zharski)")
