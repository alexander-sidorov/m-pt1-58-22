# pragma: no cover


from django.http import HttpRequest
from django.http import HttpResponse


def handle_alexander_sidorov(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello from Alexander Sidorov")
