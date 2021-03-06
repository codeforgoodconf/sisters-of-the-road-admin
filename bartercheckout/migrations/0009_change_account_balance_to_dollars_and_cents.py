# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-06 05:23
from __future__ import unicode_literals

import decimal

from django.db import migrations


def forwards_function(apps, schema_editor):
    """Change current balance column from cents to dollars and cents.
    """
    with decimal.localcontext() as c:
        c.prec = 6

        BarterAccount = apps.get_model('bartercheckout', 'BarterAccount')
        for account in BarterAccount.objects.all():
            account.balance /= 100.0
            account.save()

        BarterEvent = apps.get_model('bartercheckout', 'BarterEvent')
        for event in BarterEvent.objects.all():
            event.amount /= 100
            event.save()


def backwards_function(apps, schema_editor):
    """Revert back from dollars and cents to cents only.
    """
    with decimal.localcontext() as c:
        c.prec = 6

        BarterAccount = apps.get_model('bartercheckout', 'BarterAccount')
        for account in BarterAccount.objects.all():
            account.balance *= 100
            account.save()

        BarterEvent = apps.get_model('bartercheckout', 'BarterEvent')
        for event in BarterEvent.objects.all():
            event.amount *= 100


class Migration(migrations.Migration):
    dependencies = [
        ('bartercheckout', '0008_auto_20190105_2240'),
    ]

    operations = [
        migrations.RunPython(code=forwards_function, reverse_code=backwards_function),
    ]
