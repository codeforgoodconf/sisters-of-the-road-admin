from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import BarterAccount

def home(request):
    return render(request, 'index.html', {})
	
def account_add(request, account_id):
    ba = BarterAccount.objects.filter(id=account_id)[0]
    ba.add_account(1)
    ba.save()
    print(ba.balance)
    return JsonResponse({"foo":"bar"})

def account_subtract(request):
    return JsonResponse({"foo":"bar"})