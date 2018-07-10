# codding=utf-8

from django.http import HttpResponse, request
from django.shortcuts import render


def base_init(request):
    context = {"title": "myblog", "body": "hello, python", "list": range(10)}
    return render(request, "index.html", context)
