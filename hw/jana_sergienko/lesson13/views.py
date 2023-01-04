from django.http import HttpRequest
from django.http import HttpResponse


def handle_jana_sergienko(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello from Jana Sergienko")
