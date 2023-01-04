from django.http import HttpRequest, HttpResponse


def hello_world_vadim_zharski(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello from app (vadim_zharski)")
