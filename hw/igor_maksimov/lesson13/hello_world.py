from django.http import HttpRequest, HttpResponse

def handle_hello_world(request: HttpRequest):
    return HttpResponse("hello world")