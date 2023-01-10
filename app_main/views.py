from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render


def main(request: HttpRequest) -> HttpResponse:
    page = render(request, "app_main/main_index.html")
    return page
