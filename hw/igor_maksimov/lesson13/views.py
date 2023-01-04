from django.http import HttpRequest, HttpResponse


def handle_igor_maksimov(request: HttpRequest):
    return HttpResponse("hello from Igor Maksimov")
