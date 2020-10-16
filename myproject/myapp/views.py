# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")
def hello(request):
    return render(request, "hello.html")


def render_greaph(request):
    print("inside render_greaph function")
    print(request.POST)
    start_date = request.POST["start_date"]
    end_date = request.POST["end_date"]
