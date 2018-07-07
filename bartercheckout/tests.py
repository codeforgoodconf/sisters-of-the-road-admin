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
        summer = BarterAccount.objects.get(customer_name="Summer Salt")
        self.assertTrue(summer)
        summers_id = summer.id
        request = self.factory.post('/account/{}/credit'.format(summers_id), json.dumps({'amount': 250}), content_type='application/json')
        response = credit(request, summers_id)
        print(response)
        """
        If user exists test that the add() method is called.
        """
        summer.refresh_from_db()
        self.assertEquals(summer.balance, 450)
        """
        If exists, credit amount valid, no errors, credit event created.
        """
        creditevent = BarterEvent.objects.get(event_type="Add", amount=250)
        self.assertTrue(creditevent)
        """
        If exists, credit amount NOT valid, json returned describing error.
        """
        
        
    def test_invalid_BarterAccount(self):
        """
        If user does not exist, test proper error response returned.
        """


        """
        response = self.credit()
        """
    
