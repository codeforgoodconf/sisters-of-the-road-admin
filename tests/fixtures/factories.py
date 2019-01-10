import random
from decimal import Decimal

import factory
from djmoney.money import Money
from factory.django import DjangoModelFactory
from faker import Faker
from faker.providers import BaseProvider

from bartercheckout.models import BarterAccount
from tests.util import MonkeyPatch


class BaseDjangoModelFactory(DjangoModelFactory):
    class Meta:
        abstract = True

    @classmethod
    def _create(cls, model_cls, *args, **kwargs):
        """Allow auto_now_add fields to be set"""
        passed_fields = set(kwargs)
        auto_now_add_fields = [
            field
            for field in model_cls._meta.concrete_fields
            if field.name in passed_fields and (
                    getattr(field, 'auto_now_add', False) or
                    getattr(field, 'auto_now', False)
            )
        ]

        # We temporarily disable auto_now and auto_now_add for any explicitly
        # passed fields. This allows us to pass values directly to
        # Manager.create, without having a separate update & save() step.
        with MonkeyPatch() as mp:
            for field in auto_now_add_fields:
                mp.setattr(field, 'auto_now', False)
                mp.setattr(field, 'auto_now_add', False)

            instance = super()._create(model_cls, *args, **kwargs)

        return instance


fake = Faker()


class Provider(BaseProvider):
    def money(self):
        amounts = [x / 100 for x in range(2000, 3001, 25)]
        return Money(random.choice(amounts), 'USD')


fake.add_provider(Provider)


def add_events(obj, create, extracted, **kwargs):
    if not create:
        return

    amounts = [x / 100 for x in range(100, 501, 25)]
    for i in range(6):
        if i % 2:
            to_add = random.choice([
                amount for amount
                in amounts
                if obj.balance.amount + Decimal(amount) <= 50
            ])
            obj.add(to_add)
        else:
            to_subtract = random.choice([
                amount for amount
                in amounts
                if obj.balance.amount - Decimal(amount) >= 0
            ])
            obj.subtract(to_subtract)


class BarterAccountFactory(BaseDjangoModelFactory):
    class Meta:
        model = BarterAccount

    customer_name = factory.Faker('name')
    balance = fake.money()

    add_events = factory.PostGeneration(add_events)
