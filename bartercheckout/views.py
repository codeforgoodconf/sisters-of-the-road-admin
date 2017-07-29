from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from .models import BarterAccount

def home(request):
    return render(request, 'index.html', {})
	
def account_add(request, account_id):
    ba = BarterAccount.objects.filter(id=account_id)
    if len(ba) > 0:
        ba = ba[0]
        ba.add_account(1)
        ba.save()
        return JsonResponse({'result': 'ok'})
    else:
        return JsonResponse({'error': 'noSuchAccount'})

def account_subtract(request):
    return JsonResponse({"foo":"bar"})

from django.http import HttpResponse

def home(request):
    return render(request, 'index.html', {})

def hello_api(request):
    return HttpResponse('Hello')

def account(request):
    return

