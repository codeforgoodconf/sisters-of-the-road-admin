import json

from django.test import TestCase
from django.test.client import RequestFactory
from djmoney.money import Money

from bartercheckout.models import BarterAccount, BarterEvent
from bartercheckout.views.barter_account import credit


# Create your tests here.
class CreditTest(TestCase):

    def setUp(self):
        # Add account to db
        summer = BarterAccount.objects.create(customer_name='Summer Salt', balance=Money(2.00, 'USD'))
        summer.save()

        self.factory = RequestFactory()

    def test_BarterAccount_exists_and_adds(self):
        # Test that user exists.
        summer = BarterAccount.objects.get(customer_name='Summer Salt')
        # Test that the add() method was called.
        summers_id = summer.id
        request = self.factory.post(f'/account/{summers_id}/credit',
                                    json.dumps({'amount': 2.50}),
                                    content_type='application/json')
        response = credit(request, summers_id)
        summer.refresh_from_db()
        self.assertEquals(summer.balance, Money(4.50, 'USD'))
        # Test that a credit event was created.
        creditevent = BarterEvent.objects.get(event_type='Add', amount=2.50)
        self.assertTrue(creditevent)
        # If exists, credit amount NOT valid, json returned describing error.
        request = self.factory.post(f'/account/{summers_id}/credit',
                                    json.dumps({'amount': 2.55}),
                                    content_type='application/json')
        response = credit(request, summers_id)
        self.assertJSONEqual(response.content, {'result': 'input_error'})
        summer.refresh_from_db()
        self.assertEquals(summer.balance, Money(4.50, 'USD'))

    def test_error_invalid_BarterAccount(self):
        # If user does not exist, test proper error response returned.
        fake_id = 998
        request = self.factory.post(f'/account/{fake_id}/credit',
                                    json.dumps({'amount': 2.50}),
                                    content_type='application/json')
        response = credit(request, fake_id)
        self.assertJSONEqual(response.content, {'error': 'noSuchAccount'})
