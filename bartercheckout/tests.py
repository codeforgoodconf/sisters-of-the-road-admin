import json
from django.test import TestCase
from .models import BarterEvent, BarterAccount
from django.test.client import RequestFactory
from .views import credit


# Create your tests here.
class CreditTest(TestCase):
    
    def setUp(self):
        """
        Add account to db
        """
        summer = BarterAccount.objects.create(customer_name="Summer Salt", balance=200)
        summer.save()
        
        self.factory = RequestFactory()

    def test_BarterAccount_exists_and_adds(self):
        """
        Test that user exists.
        """
        summer = BarterAccount.objects.get(customer_name="Summer Salt")
        self.assertTrue(summer)
        """
        Test that the add() method was called.
        """
        summers_id = summer.id
        request = self.factory.post('/account/{}/credit'.format(summers_id), json.dumps({'amount': 250}), content_type='application/json')
        response = credit(request, summers_id)
        summer.refresh_from_db()
        self.assertEquals(summer.balance, 450)
        """
        Test that a credit event was created.
        """
        creditevent = BarterEvent.objects.get(event_type="Add", amount=250)
        self.assertTrue(creditevent)
        """
        If exists, credit amount NOT valid, json returned describing error.
        """
        request = self.factory.post('/account/{}/credit'.format(summers_id), json.dumps({'amount': 255}), content_type='application/json')
        response = credit(request, summers_id)
        self.assertJSONEqual(response.content, {'result': 'input_error'})
        summer.refresh_from_db()
        self.assertEquals(summer.balance, 450)
        

    def test_error_invalid_BarterAccount(self):
        """
        If user does not exist, test proper error response returned.
        """
        request = self.factory.post('/account/{}/credit'.format(998), json.dumps({'amount': 250}), content_type='application/json')
        response = credit(request, 998)
        self.assertJSONEqual(response.content, {'error': 'noSuchAccount'})
    
