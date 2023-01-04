from django.http import HttpRequest
from django.http import HttpResponse

def helloworld(request: HttpRequest) -> HttpResponse:
    return HttpResponse("hello from app")

# Create your views here.
