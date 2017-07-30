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


def hello_api(request):
    return HttpResponse('Hello')