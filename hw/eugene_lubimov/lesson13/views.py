from django.http import HttpRequest
from django.http import HttpResponse


def my_view(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello from Eugene Lubimov")
