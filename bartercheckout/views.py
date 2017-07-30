"""
API endpoints
"""

import json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .models import BarterAccount

def home(request):
    """
    The home page
    """
    return render(request, 'index.html', {})

def list_accounts(request):
    query_result = BarterAccount.objects.all()
    account_list = []
    for account in query_result:
            account_dict = {'name': account.customer_name,
                           'balance': account.balance,
                           'last_add': account.last_add or 'Nothing yet!',
                           'last_subtract': account.last_subtract or 'Nothing yet!'}
            account_list.append(account_dict)
    return JsonResponse(account_list, safe=False)

def search_accounts(request):
    search_text = request.GET.get('q')
    query_result = BarterAccount.objects.filter(customer_name__icontains=search_text)
    account_list = []
    for account in query_result:
            account_dict = {'name': account.customer_name,
                           'balance': account.balance,
                           'last_add': account.last_add or 'Nothing yet!',
                           'last_subtract': account.last_subtract or 'Nothing yet!'}
            account_list.append(account_dict)
    return JsonResponse(account_list, safe=False)

def add(request, account_id):
    """
    Add a dollar amount to the specified account
    """
    ba = BarterAccount.objects.filter(id=account_id)
    if len(ba) > 0:
        ba = ba[0]
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)
        newBalance = ba.add(body_data['amount'])
        ba.save()
        return JsonResponse({'result': 'ok'})
    else:
        return JsonResponse({'error': 'noSuchAccount'})


def subtract(request, account_id):
    """
    Subtract a dollar amount to the specified account
    """
    ba = BarterAccount.objects.filter(id=account_id)
    if len(ba) > 0:
        ba = ba[0]
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)
        ba.subtract(body_data['amount'])
        ba.save()
        return JsonResponse({'result': 'ok'})
    else:
        return JsonResponse({'error': 'noSuchAccount'})


