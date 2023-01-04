from django.http import HttpRequest
from django.http import HttpResponse


def hello_mk(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello from mikitakarman's app!")
