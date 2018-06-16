from django.test import TestCase
from .models import BarterEvent, BarterAccount
from django.test.client import RequestFactory

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
        request = self.factory.get('/account/{}/credit'.format(summers_id))
        print(request)
        """
        If user exists test that the add() method is called.
        """
        "call add method"
        """
        If exists, credit amount valid, no errors, credit event created.
        """
        """
        If exists, credit amount NOT valid, json returned describing error.
        """
        
    def test_credit_methods(self):
        """
        If user does not exist, test proper error response returned.
        """

    
        """
        response = self.credit()
        """
    
