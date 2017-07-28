from django.shortcuts import render

def home(request):
    return render(request, 'index.html', {})

def account(request):
    return render(request, 'account.html', {})

def buymeal(request):
    return render(request, 'buymeal.html', {})

def addcredit(request):
    return render(request, 'addcredit.html', {})