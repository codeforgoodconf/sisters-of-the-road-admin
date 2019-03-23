"""
API endpoints
"""

import json


from django.http import JsonResponse
from django.shortcuts import render

from .models import AmountInputError, BalanceLimitError, BarterAccount, BarterEvent


def home(request):
    """
    The home page
    """
    return render(request, 'index.html', {})


def list_accounts(request):
    query_result = BarterAccount.objects.all()
    account_list = []
    for account in query_result:
        account_dict = {
            'account_id': account.id,
            'name': account.customer_name,
            'balance': account.balance.amount,
            'last_add': account.last_add or 'Nothing yet!',
            'last_subtract': account.last_subtract or 'Nothing yet!'
        }
        account_list.append(account_dict)
    return JsonResponse(account_list, safe=False)


def search_accounts(request):
    search_text = request.GET.get('q')
    query_result = BarterAccount.objects.filter(customer_name__icontains=search_text)
    account_list = []
    for account in query_result:
        account_dict = {
            'account_id': account.id,
            'name': account.customer_name,
            'balance': account.balance.amount,
            'last_add': account.last_add or 'Nothing yet!',
            'last_subtract': account.last_subtract or 'Nothing yet!'
        }
        account_list.append(account_dict)
    return JsonResponse(account_list, safe=False)


def credit(request, account_id):
    """
    Add credit to a BarterAccount and create a BarterEvent
    as a record of the transaction.
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
        try:
            newBalance = account.add(amount)
        except BalanceLimitError:
            return JsonResponse({'error': 'limit_error'})
        except AmountInputError:
            return JsonResponse({'error': 'input_error'})
        account.save()

        # Create event
        data = {'barter_account': account, 'event_type': 'Add', 'amount': amount}
        event = BarterEvent(**data)
        event.save()

        account_dict = {
            'account_id': account.id,
            'name': account.customer_name,
            'balance': account.balance.amount,
            'last_add': account.last_add or 'Nothing yet!',
            'last_subtract': account.last_subtract or 'Nothing yet!'
        }

        return JsonResponse(account_dict)
    else:
        return JsonResponse({'error': 'noSuchAccount'})


def buy_meal(request, account_id):
    """
    Spend from a BarterAccount to purchase a meal and
    create a BarterEvent as a record of the transaction.
    """
    accounts = BarterAccount.objects.filter(id=account_id)
    if accounts:
        account = accounts[0]
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)
        amount = body_data['amount']
        initials = body_data['initials']

        # Update the barter account
        try:
            newBalance = account.subtract(amount)
        except BalanceLimitError:
            return JsonResponse({'error': 'limit_error'})
        except AmountInputError:
            return JsonResponse({'error': 'input_error'})
        account.save()

        # Create event
        data = {'barter_account': account, 'event_type': 'Buy_meal', 'amount': amount, 'initials': initials }
        event = BarterEvent(**data)
        event.save()

        account_dict = {
            'account_id': account.id,
            'name': account.customer_name,
            'balance': account.balance.amount,
            'last_add': account.last_add or 'Nothing yet!',
            'last_subtract': account.last_subtract or 'Nothing yet!'
        }

        return JsonResponse(account_dict)
    else:
        return JsonResponse({'error': 'noSuchAccount'})


def buy_card(request, account_id):

    """
    Spend from a BarterAccount to purchase a barter card and
    create a BarterEvent as a record of the transaction.
    """
    accounts = BarterAccount.objects.filter(id=account_id)
    if accounts:
        account = accounts[0]
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)
        amount = body_data['amount']
        initials = body_data['initials']


        # Update the barter account
        try:
            newBalance = account.subtract(amount)
        except BalanceLimitError:
            return JsonResponse({'error': 'limit_error'})
        except AmountInputError:
            return JsonResponse({'error': 'input_error'})
        account.save()

        # Create event
        data = {'barter_account': account, 'event_type': 'Buy_card', 'amount': amount, 'initials': initials}
        event = BarterEvent(**data)
        event.save()
        

        account_dict = {
            'account_id': account.id,
            'name': account.customer_name,
            'balance': account.balance.amount,
            'last_add': account.last_add or 'Nothing yet!',
            'last_subtract': account.last_subtract or 'Nothing yet!'
        }

        return JsonResponse(account_dict)
    else:
        return JsonResponse({'error': 'noSuchAccount'})
