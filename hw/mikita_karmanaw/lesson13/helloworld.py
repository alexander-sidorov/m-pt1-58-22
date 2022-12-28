from django.http import HttpRequest, HttpResponse


def mikita_karmanaw_helloworld(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello, world!")
