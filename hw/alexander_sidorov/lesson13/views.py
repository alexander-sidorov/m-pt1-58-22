from django.http import HttpRequest, HttpResponse


def handle_alexander_sidorov(request: HttpRequest):
    return HttpResponse("Hello world")
