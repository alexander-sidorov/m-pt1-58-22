from django.http import HttpRequest
from django.http import HttpResponse


def handle_eugene_ladyko(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello from Eugene Ladyko")
