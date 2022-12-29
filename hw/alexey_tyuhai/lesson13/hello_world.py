from django.http import HttpRequest, HttpResponse


def handle_alexey_tuyhai(request: HttpRequest):
    return HttpResponse("Hello world")
