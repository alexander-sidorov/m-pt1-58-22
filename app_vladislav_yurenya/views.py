from django.http import HttpResponse,HttpRequest


def helloworld(request: HttpRequest) -> HttpResponse:
    return HttpResponse('HELLO FROM APP!')
