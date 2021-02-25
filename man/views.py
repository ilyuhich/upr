from django.shortcuts import render
from django.http import request


# Create your views here.

def hello(request):
    return render(request, 'man/base.html')
