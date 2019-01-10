from datetime import date

from django.conf import settings
from django.db import models
from djmoney.models.fields import MoneyField
from djmoney.money import Money
from factory.django import get_model

from bartercheckout.custom_errors import AmountInputError, BalanceLimitError

balance_limit = Money(settings.BALANCE_LIMIT, 'USD')


class BarterAccount(models.Model):
    class Meta:
        ordering = ['customer_name']

    customer_name = models.CharField(max_length=100)
    balance = MoneyField(max_digits=6, decimal_places=2, default_currency='USD', default=0.0)
    last_add = models.DateField(null=True)
    last_subtract = models.DateField(null=True)

    def add(self, amount):
        if amount <= 0 or (amount * 100) % 25 != 0:
            raise AmountInputError("Invalid amount")

        amount = Money(amount, 'USD')

        if self.balance + amount > balance_limit:
            raise BalanceLimitError(
                f"Balance can't go above $50. "
                f"Current balance {self.balance}. "
                f"You can add up to {balance_limit - self.balance}"
            )
        else:
            self.balance += amount
            self.last_add = date.today()
            barter_event = get_model('bartercheckout', 'BarterEvent')  # Prevent circular import
            barter_event.objects.create(barter_account=self, amount=amount)

    def subtract(self, amount):
        if amount <= 0 or (amount * 100) % 25 != 0:
            raise AmountInputError("Invalid amount")

        amount = Money(amount, 'USD')

        if self.balance - amount < Money(0, 'USD'):
            raise BalanceLimitError(f"Balance can't go below {Money(0, 'USD')}")
        else:
            self.balance -= amount
            self.last_subtract = date.today()
            barter_event = get_model('bartercheckout', 'BarterEvent')  # Prevent circular import
            barter_event.objects.create(barter_account=self, amount=amount)

    def __repr__(self):
        return (
            f'BarterAccount(customer_name="{self.customer_name}", '
            f'balance={self.balance!r}, '
            f'last_add={self.last_add!r}, '
            f'last_subtract={self.last_subtract!r})'
        )

    def __str__(self):
        return f'id: {self.id}, Name: {self.customer_name}, Current Balance: {self.balance}'

    @property
    def account_balance(self):
        return f'{self.balance}' if self.balance else ''
