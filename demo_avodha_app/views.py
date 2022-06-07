from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def demo(req):
    return  HttpResponse("<h1>Hello World</h1>")