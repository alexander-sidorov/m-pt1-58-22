from django.http import HttpRequest, HttpResponse


def my_view(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello from Eugene Lubimov")