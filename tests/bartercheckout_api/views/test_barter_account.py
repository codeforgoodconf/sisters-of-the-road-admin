import decimal
from decimal import Decimal
from typing import Any, Dict

import pytest
from django.conf import settings
from djmoney.money import Money
from rest_framework.reverse import reverse

from bartercheckout.models import BarterAccount
from tests.fixtures.utils import lambda_fixture, precondition_fixture, static_fixture
from tests.util.decorators import pluralized
from ..base import (
    Returns200,
    Returns400,
    UsesDetailEndpoint,
    UsesGetMethod,
    UsesListEndpoint,
    UsesPostMethod,
    ViewSetTest,
)

decimal.getcontext().prec = 4


def express_barter_account(barter_account: BarterAccount) -> Dict[str, Any]:
    if barter_account:
        return {
            'id': barter_account.id,
            'customer_name': barter_account.customer_name,
            'balance': f'{barter_account.balance.amount:0.2f}',
            'last_add': str(barter_account.last_add),
            'last_subtract': str(barter_account.last_subtract),
        }


express_barter_accounts = pluralized(express_barter_account)

my_barter_account = lambda_fixture(lambda barter_account_factory: barter_account_factory.create(), autouse=True)
barter_accounts = lambda_fixture(lambda barter_account_factory: barter_account_factory.create_batch(5), autouse=True)


@pytest.mark.django_db
class TestBarterAccountApi(ViewSetTest):
    list_url = lambda_fixture(lambda: reverse('accounts-list'))
    detail_url = lambda_fixture(
        lambda my_barter_account: reverse('accounts-detail', kwargs={'pk': my_barter_account.id})
    )

    class TestList(
        UsesGetMethod,
        UsesListEndpoint,

        Returns200,
    ):
        def it_lists_all_barter_accounts(self, my_barter_account, barter_accounts, json):
            expected = express_barter_accounts(
                *sorted([my_barter_account] + barter_accounts, key=lambda account: account.customer_name)
            )
            actual = json
            assert expected == actual

    class TestRetrieve(
        UsesGetMethod,
        UsesDetailEndpoint,

        Returns200,
    ):
        def it_gets_a_single_barter_account(self, my_barter_account, json):
            expected = express_barter_account(my_barter_account)
            actual = json
            assert expected == actual

    class TestCreditAccount(
        UsesPostMethod,
    ):
        url = lambda_fixture(lambda detail_url: f'{detail_url}/credit')
        balance_before_call = precondition_fixture(lambda my_barter_account: my_barter_account.balance.amount)

        class ContextValidInput(
            Returns200,
        ):
            data = static_fixture({'amount': 2.25})

            def it_adds_credit_to_my_barter_account(self, my_barter_account, balance_before_call, json):
                assert json == {'balance': balance_before_call + Decimal(2.25)}
                actual = BarterAccount.objects.get(id=my_barter_account.id)
                assert actual.balance.amount == balance_before_call + Decimal(2.25)

        class ContextInvalidInput(
            Returns400,
        ):
            class ContextMaxBalanceExceeded:
                data = static_fixture({'amount': 50.00})

                def it_does_not_allow_balance_to_go_above_50(self, my_barter_account, balance_before_call, json):
                    expected_message = (
                        f"Balance can't go above $50. "
                        f"Current balance {my_barter_account.balance}. "
                        f"You can add up to {Money(settings.BALANCE_LIMIT, 'USD') - my_barter_account.balance}"
                    )
                    balance_after_call = BarterAccount.objects.get(id=my_barter_account.id).balance.amount

                    assert json == {'result': 'limit_error', 'message': expected_message}
                    assert balance_before_call == balance_after_call

            class ContextInvalidAmount:
                class ContextNegativeAmount:
                    data = static_fixture({'amount': -3.00})

                    def it_does_not_allow_negative_amounts(self, my_barter_account, balance_before_call, json):
                        balance_after_call = BarterAccount.objects.get(id=my_barter_account.id).balance.amount

                        assert json == {'result': 'input_error', 'message': 'Invalid amount'}
                        assert balance_before_call == balance_after_call

                class ContextAmountNotRoundedToNearestQuarter:
                    data = static_fixture({'amount': 5.33})

                    def it_does_not_allow_amounts_not_rounded_to_25c(
                            self, my_barter_account, balance_before_call, json
                    ):
                        balance_after_call = BarterAccount.objects.get(id=my_barter_account.id).balance.amount

                        assert json == {'result': 'input_error', 'message': 'Invalid amount'}
                        assert balance_before_call == balance_after_call

    class TestBuyMeal(
        UsesPostMethod,
    ):
        url = lambda_fixture(lambda detail_url: f'{detail_url}/buy_meal')
        balance_before_call = precondition_fixture(lambda my_barter_account: my_barter_account.balance.amount)

        class ContextValidInput(
            Returns200,
        ):
            data = static_fixture({'amount': 1.50})

            def it_subtracts_credit_from_my_barter_account(self, my_barter_account, balance_before_call, json):
                assert json == {'balance': balance_before_call - Decimal(1.50)}
                actual = BarterAccount.objects.get(id=my_barter_account.id)
                assert actual.balance.amount == balance_before_call - Decimal(1.50)

        class ContextInvalidInput(
            Returns400,
        ):
            class ContextMaxBalanceExceeded:
                data = static_fixture({'amount': 50.00})

                def it_does_not_allow_balance_to_go_negative(self, my_barter_account, balance_before_call, json):
                    expected_message = f"Balance can't go below {Money(0, 'USD')}"
                    balance_after_call = BarterAccount.objects.get(id=my_barter_account.id).balance.amount

                    assert json == {'result': 'limit_error', 'message': expected_message}
                    assert balance_before_call == balance_after_call

            class ContextInvalidAmount:
                class ContextNegativeAmount:
                    data = static_fixture({'amount': -3.00})

                    def it_does_not_allow_negative_amounts(self, my_barter_account, balance_before_call, json):
                        balance_after_call = BarterAccount.objects.get(id=my_barter_account.id).balance.amount

                        assert json == {'result': 'input_error', 'message': 'Invalid amount'}
                        assert balance_before_call == balance_after_call

                class ContextAmountNotRoundedToNearestQuarter:
                    data = static_fixture({'amount': 5.33})

                    def it_does_not_allow_amounts_not_rounded_to_25c(
                            self, my_barter_account, balance_before_call, json
                    ):
                        balance_after_call = BarterAccount.objects.get(id=my_barter_account.id).balance.amount

                        assert json == {'result': 'input_error', 'message': 'Invalid amount'}
                        assert balance_before_call == balance_after_call

    class TestBuyCard(
        UsesPostMethod,
    ):
        url = lambda_fixture(lambda detail_url: f'{detail_url}/buy_card')
        balance_before_call = precondition_fixture(lambda my_barter_account: my_barter_account.balance.amount)

        class ContextValidInput(
            Returns200,
        ):
            data = static_fixture({'amount': 1.50})

            def it_subtracts_credit_from_my_barter_account(self, my_barter_account, balance_before_call, json):
                assert json == {'balance': balance_before_call - Decimal(1.50)}
                actual = BarterAccount.objects.get(id=my_barter_account.id)
                assert actual.balance.amount == balance_before_call - Decimal(1.50)

        class ContextInvalidInput(
            Returns400,
        ):
            class ContextMaxBalanceExceeded:
                data = static_fixture({'amount': 50.00})

                def it_does_not_allow_balance_to_go_negative(self, my_barter_account, balance_before_call, json):
                    expected_message = f"Balance can't go below {Money(0, 'USD')}"
                    balance_after_call = BarterAccount.objects.get(id=my_barter_account.id).balance.amount

                    assert json == {'result': 'limit_error', 'message': expected_message}
                    assert balance_before_call == balance_after_call

            class ContextInvalidAmount:
                class ContextNegativeAmount:
                    data = static_fixture({'amount': -3.00})

                    def it_does_not_allow_negative_amounts(self, my_barter_account, balance_before_call, json):
                        balance_after_call = BarterAccount.objects.get(id=my_barter_account.id).balance.amount

                        assert json == {'result': 'input_error', 'message': 'Invalid amount'}
                        assert balance_before_call == balance_after_call

                class ContextAmountNotRoundedToNearestQuarter:
                    data = static_fixture({'amount': 5.33})

                    def it_does_not_allow_amounts_not_rounded_to_25c(
                            self, my_barter_account, balance_before_call, json
                    ):
                        balance_after_call = BarterAccount.objects.get(id=my_barter_account.id).balance.amount

                        assert json == {'result': 'input_error', 'message': 'Invalid amount'}
                        assert balance_before_call == balance_after_call
