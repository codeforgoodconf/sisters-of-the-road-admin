import decimal
from datetime import date

from django.db import models

decimal.getcontext().prec = 2


class BalanceLimitError(Exception):
    """Raise when account balance exceeds limits"""


class AmountInputError(Exception):
    """Raise when amount entered is invalid"""


# Create your models here.
class BarterEvent(models.Model):
    barter_account = models.ForeignKey('BarterAccount')

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

    event_time = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField(default=0)

    @property
    def customer_name(self):
        return self.barter_account.customer_name

    @property
    def transaction_amount(self):
        assert type(self.amount) == int
        return f'${self.amount:,.2f}'

    # staff_id = models.ForeignKey()

    def __str__(self):
        return f'Barter event ID {self.id} for {self.customer_name}'


class BarterAccount(models.Model):
    customer_name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=4, decimal_places=2, default=0.0)
    last_add = models.DateField(null=True)
    last_subtract = models.DateField(null=True)

    def add(self, amount):
        if amount < 0 or (amount * 100) % 25 != 0:
            raise AmountInputError("Invalid amount")

        dec_amount = decimal.Decimal(amount)
        if self.balance + dec_amount > 50:
            raise BalanceLimitError(f"Balance can't go above $50. Current balance ${self.balance}. You can add up to "
                                    f"${decimal.Decimal(50.0) - self.balance}")
        else:
            self.balance += dec_amount
            self.last_add = date.today()
            return self.balance

    def subtract(self, amount):
        if amount < 0 or amount % 25 != 0:
            raise AmountInputError("Invalid amount")

        dec_amount = decimal.Decimal(amount)
        if self.balance - dec_amount < 0:
            raise BalanceLimitError("Balance can't go below $0")
        else:
            self.balance -= dec_amount
            self.last_subtract = date.today()
            return self.balance


    def __repr__(self):
        return (
            f'BarterAccount(customer_name="{self.customer_name}", '
            f'balance={self.balance}, '
            f'last_add={self.last_add}, '
            f'last_subtract={self.last_subtract})'
        )

    def __str__(self):
        return f'Account: {self.customer_name}'

    @property
    def account_balance(self):
        assert type(self.balance) == int
        return f'${self.balance:,.2f}' if self.balance else ''
