"""
API endpoints
"""

import json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .models import BarterAccount, BarterEvent

def home(request):
    """
    The home page
    """
    return render(request, 'index.html', {})

def list_accounts(request):
    query_result = BarterAccount.objects.all()
    account_list = []
    for account in query_result:
            account_dict = {'account_id': account.id,
                            'name': account.customer_name,
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
            account_dict = {'account_id': account.id,
                            'name': account.customer_name,
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


def credit(request, account_id):
    """
    Add a dollar amount to the specified account
    -Get account
    -Add money
    -Create event
    """
    accounts = BarterAccount.objects.filter(id=account_id)
    # The filter method returns None if there's no account that matches the id
    # If accounts equals None, return an error
    if accounts:
        # The filter method returns a list. There should only be 1 item
        # in this list because ID is a primary key. But we still need to
        # grab the first item from the list.
        account = accounts[0]

        # Get amount to add from request
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)
        amount = body_data['amount']

        # Update the barter account
        newBalance = account.add(amount)
        account.save()

        # Create event
        data = {'barter_account': account, 'event_type': 'Add', 'amount': amount}
        event = BarterEvent(**data)
        event.save()

        return JsonResponse({'result': 'ok'})
    else:
        return JsonResponse({'error': 'noSuchAccount'})

def buy_meal(request, account_id):
    """
    Subtract a dollar amount from the specified account
    -Get account
    -Subtract money
    -Create event
    """
    accounts = BarterAccount.objects.filter(id=account_id)
    if accounts:
        account = accounts[0]
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)
        amount = body_data['amount']

        # Update the barter account
        newBalance = account.subtract(amount)
        account.save()

        # Create event
        data = {'barter_account': account, 'event_type': 'Buy_meal', 'amount': amount}
        event = BarterEvent(**data)
        event.save()

        return JsonResponse({'result': 'ok'})
    else:
        return JsonResponse({'error': 'noSuchAccount'})