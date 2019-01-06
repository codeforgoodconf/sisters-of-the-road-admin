import decimal

from django.db import models
from djmoney.models.fields import MoneyField

decimal.getcontext().prec = 4


class BarterEvent(models.Model):
    ADD = 'Add'
    BUY_MEAL = 'Buy_meal'
    BUY_CARD = 'Buy_card'
    NOTE = 'Note'

    EVENT_TYPE_CHOICES = (
        (ADD, 'Add'),
        (BUY_MEAL, 'Buy_meal'),
        (BUY_CARD, 'Buy_card'),
        (NOTE, 'Note'),
    )

    event_type = models.CharField(
        max_length=20,
        choices=EVENT_TYPE_CHOICES,
        default=BUY_MEAL,
    )

    barter_account = models.ForeignKey('BarterAccount', related_name='barter_events', on_delete=models.CASCADE)
    event_time = models.DateTimeField(auto_now_add=True)
    amount = MoneyField(max_digits=6, decimal_places=2, default_currency='USD', default=0.0)

    @property
    def customer_name(self):
        return self.barter_account.customer_name

    @property
    def transaction_amount(self):
        return f'{self.amount}'

    def __repr__(self):
        return f'BarterEvent(event_time={self.event_time!r}, amount={self.amount!r}'

    def __str__(self):
        return f'Barter event ID {self.id} for {self.customer_name}'
