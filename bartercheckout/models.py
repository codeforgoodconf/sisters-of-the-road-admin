from django.db import models
from datetime import date

# Create your models here.
class BarterEvent(models.Model):
    barter_account = models.ForeignKey('BarterAccount')

    ADD = 'Add'
    SUBTRACT = 'Subtract'
    NOTE = 'Note'

    EVENT_TYPE_CHOICES = (
        (ADD, 'Add'),
        (SUBTRACT, 'Subtract'),
        (NOTE, 'Note'),
        )

    event_type = models.CharField(
        max_length=20,
        choices = EVENT_TYPE_CHOICES,
        default = SUBTRACT,
        )

    event_time = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=4, decimal_places=2, default=0.00)
    #staff_id = models.ForeignKey()
    def __str__(self):
        if self.event_type == 'Add':
            message = '{} added to account on {}'.format(self.barter_account.customer_name, self.event_time)
        else:
            message = '{} subtracted from account on {}'.format(self.barter_account.customer_name, self.event_time)
        return message


class BarterAccount(models.Model):
    customer_name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    last_add = models.DateField(null=True)
    last_subtract = models.DateField(null=True)

    def add(self, amount):
        data = {'barter_account':self, 'event_type':'Add', 'amount':amount}
        event = BarterEvent(**data)
        self.last_add = date.today()
        self.balance += amount
        event.save()
        return self.balance

    def subtract(self, amount):
        data = {'barter_account':self, 'event_type':'Subtract', 'amount':amount}
        event = BarterEvent(**data)
        self.last_subtract = date.today()
        self.balance -= amount
        event.save()
        return self.balance

    def __str__(self):
        return 'Account: {}'.format(self.customer_name)
