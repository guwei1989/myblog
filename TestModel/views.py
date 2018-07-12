# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from TestModel.models import user
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json


# Create your views here.
def index(request):
    return render(request, "base.html", {"a": 1, "b": 2})


@csrf_exempt
def save_user_info(request):
    if request.method == "POST":
        name = request.POST.get('user')

        pwd = request.POST.get('password')

        auth = request.POST.get('auth')

        time = request.POST.get('time')

        obj = user(account=name, authority=auth, passwd=pwd, registTime=time)

        obj.save()

        return json.dumps({"result": 0})
    else:
        return json.dumps({"result": 1})
