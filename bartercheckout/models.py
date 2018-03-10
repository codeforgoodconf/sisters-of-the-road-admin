from django.db import models
from datetime import date


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
        choices = EVENT_TYPE_CHOICES,
        default = BUY_MEAL,
        )

    event_time = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField(default=0)
    #staff_id = models.ForeignKey()
    def __str__(self):
        if self.event_type == 'Add':
            action = 'added to' 
        else:
            action = 'subtracted from'
        message = '{} {} account on {}'.format(
                self.barter_account.customer_name, action,
                self.event_time.strftime("%Y-%m-%d %I:%M%p"))
        return message


class BarterAccount(models.Model):
    customer_name = models.CharField(max_length=100)
    balance = models.IntegerField(default=0)
    last_add = models.DateField(null=True)
    last_subtract = models.DateField(null=True)

    def add(self, amount): 
        if amount < 0 or amount % 25 != 0:
            raise AmountInputError("Invalid amount")
        if self.balance + amount > 5000:
            raise BalanceLimitError("Balance can't go above $50")
        else:
            self.balance += amount
            self.last_add = date.today()
            return self.balance

    def subtract(self, amount):
        if amount < 0 or amount % 25 != 0:
            raise AmountInputError("Invalid amount")
        if self.balance - amount < 0:
            raise BalanceLimitError("Balance can't go below $0")
        else:
            self.balance -= amount
            self.last_subtract = date.today()
            return self.balance

    def __str__(self):
        return 'Account: {}'.format(self.customer_name)

    @property
    def account_balance(self):
        assert type(self.balance) == int
        return '${:,.2f}'.format(self.balance/100) if self.balance else ""