import json

from django.test import Client, TestCase
from django.urls import reverse

from mixer.backend.django import mixer

from .models import BarterAccount


class TestBuyMeal(TestCase):
    def setUp(self):
        self.client = Client()
        self.barter_account = mixer.blend(BarterAccount)

    def test_valid_transaction(self):
        self.barter_account.balance = 150
        self.barter_account.save()

        response = self.client.post(
            reverse('buy_meal', kwargs={'account_id': self.barter_account.id}),
            data=json.dumps({
                'amount': 100
            }),
            content_type='application/json'
        )
        
        self.barter_account.refresh_from_db()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'{"result": "ok"}')
        self.assertEqual(self.barter_account.balance, 50)

    def test_invalid_transaction(self):
        response = self.client.post(
            reverse('buy_meal', kwargs={'account_id': self.barter_account.id}),
            data=json.dumps({
                'amount': 100
            }),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, 402)
        self.assertEqual(response.content, b'{"result": "limit_error"}')

    def test_invalid_input_transaction(self):
        response = self.client.post(
            reverse('buy_meal', kwargs={'account_id': self.barter_account.id}),
            data=json.dumps({
                'amount': 33
            }),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.content, b'{"result": "input_error"}')
        