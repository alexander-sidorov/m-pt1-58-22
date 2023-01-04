from django.http import HttpRequest
from django.http import HttpResponse


def handle_eugene_bakun(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello from Eugene Bakun")