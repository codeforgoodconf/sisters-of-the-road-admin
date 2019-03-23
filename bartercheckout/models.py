import decimal
from datetime import date

from django.db import models
from django.db.models import CASCADE
from djmoney.models.fields import MoneyField
from djmoney.money import Money

decimal.getcontext().prec = 4

BALANCE_LIMIT = Money(50, 'USD')


class BalanceLimitError(Exception):
    """Raise when account balance exceeds limits"""


class AmountInputError(Exception):
    """Raise when amount entered is invalid"""


# Create your models here.
class BarterEvent(models.Model):
    barter_account = models.ForeignKey('BarterAccount', on_delete=CASCADE)

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

    initials = models.CharField(
        max_length=20,
        default=""
    )

    event_time = models.DateTimeField(auto_now_add=True)
    amount = MoneyField(max_digits=6, decimal_places=2, default_currency='USD', default=0.0)

    @property
    def customer_name(self):
        return self.barter_account.customer_name

    @property
    def transaction_amount(self):
        return f'${self.amount:,.2f}'

    # staff_id = models.ForeignKey()

    def __repr__(self):
        return f'BarterEvent(event_time={self.event_time!r}, amount={self.amount!r}'

    def __str__(self):
        return f'Barter event ID {self.id} for {self.customer_name}'


class BarterAccount(models.Model):
    customer_name = models.CharField(max_length=100)
    balance = MoneyField(max_digits=6, decimal_places=2, default_currency='USD', default=0.0)
    last_add = models.DateField(null=True)
    last_subtract = models.DateField(null=True)

    def add(self, amount):
        if amount < 0 or (amount * 100) % 25 != 0:
            raise AmountInputError("Invalid amount")

        amount = Money(amount, 'USD')

        if self.balance + amount > BALANCE_LIMIT:
            raise BalanceLimitError(f"Balance can't go above $50. Current balance ${self.balance}. You can add up to "
                                    f"${BALANCE_LIMIT - self.balance}")
        else:
            self.balance += amount
            self.last_add = date.today()
            return self.balance

    def subtract(self, amount):
        if amount < 0 or (amount * 100) % 25 != 0:
            raise AmountInputError("Invalid amount")

        amount = Money(amount, 'USD')

        if self.balance - amount < Money(0, 'USD'):
            raise BalanceLimitError(f'Balance can\'t go below {Money(0, "USD")}')
        else:
            self.balance -= amount
            self.last_subtract = date.today()
            return self.balance

    def __repr__(self):
        return (
            f'BarterAccount(customer_name="{self.customer_name}", '
            f'balance={self.balance!r}, '
            f'last_add={self.last_add!r}, '
            f'last_subtract={self.last_subtract!r})'
        )

    def __str__(self):
        return f'Account: {self.customer_name}'

    @property
    def account_balance(self):
        return f'{self.balance}' if self.balance else ''
