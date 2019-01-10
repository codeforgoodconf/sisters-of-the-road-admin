from typing import Any, Dict

import pytest
from django.utils.dateparse import parse_date
from rest_framework.reverse import reverse

from bartercheckout.models import BarterAccount
from tests.base import UsesListEndpoint, ViewSetTest
from tests.fixtures.utils import lambda_fixture
from tests.util.decorators import pluralized

def express_barter_account(barter_account: BarterAccount) -> Dict[str, Any]:
    if barter_account:
        return {
            'id': barter_account.id,
            'customer_name': barter_account.customer_name,
            'balance': str(barter_account.balance.amount),
            'last_add': str(barter_account.last_add),
            'last_subtract': str(barter_account.last_subtract),
        }


express_barter_accounts = pluralized(express_barter_account)

barter_accounts = lambda_fixture(lambda barter_account_factory: barter_account_factory.create_batch(5), autouse=True)


@pytest.mark.django_db
class TestBarterAccountApi(ViewSetTest):
    list_url = lambda_fixture(lambda: reverse('accounts-list'))

    # detail_url = lambda_fixture(lambda: reverse('accounts-detail', kwargs={'id': 1}))

    class TestList(UsesListEndpoint):
        def test_barter_account_list_all(self, barter_accounts, json):
            expected = express_barter_accounts(*sorted(barter_accounts, key=lambda account: account.customer_name))
            actual = json
            assert expected == actual
