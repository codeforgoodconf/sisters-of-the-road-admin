from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'index.html', {})

def hello_api(request):
    return HttpResponse('Hello')

def account(request):
    return