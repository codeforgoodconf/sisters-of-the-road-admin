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

def hello_api(request):
    return HttpResponse('Hello')

def list_accounts(request):
    query_result = BarterAccount.objects.all()
    account_list = []
    for account in query_result:
    	#account.patron_name, account.balance
    	account_list.append(account)
    # print(account_list)
    return JsonResponse(account_list, safe=False)


