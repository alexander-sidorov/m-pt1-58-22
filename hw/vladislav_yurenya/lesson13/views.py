from django.http import HttpRequest, HttpResponse


def handle_vladislav_yurenya(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello from VLADISLAV YURENYA!")