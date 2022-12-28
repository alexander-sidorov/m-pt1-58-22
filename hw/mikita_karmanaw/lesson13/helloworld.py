from django.http import HttpRequest, HttpResponse


def handle_mikita_karmanaw(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello, world!")
