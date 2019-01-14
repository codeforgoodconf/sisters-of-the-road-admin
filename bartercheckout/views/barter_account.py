import decimal

import rest_framework_filters as filters
from rest_framework import serializers, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

from bartercheckout.custom_errors import AmountInputError, BalanceLimitError
from bartercheckout.models.barter_account import BarterAccount

decimal.getcontext().prec = 4


class BarterAccountFilter(filters.FilterSet):
    class Meta:
        model = BarterAccount
        fields = {
            'customer_name': '__all__',
            'balance': '__all__',
            'last_add': '__all__',
            'last_subtract': '__all__',
        }

    name = filters.CharFilter(field_name='customer_name', lookup_expr='icontains', label='Customer Name')

    o = filters.OrderingFilter(
        fields=['customer_name']
    )


class BarterAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = BarterAccount
        fields = ['id', 'customer_name', 'balance', 'last_add', 'last_subtract']


class BarterAccountViewSet(viewsets.ModelViewSet):
    queryset = BarterAccount.objects.all()
    serializer_class = BarterAccountSerializer
    filterset_class = BarterAccountFilter

    def update_balance_and_add_event(self, request, pk, event_type):
        """Utility method that updates the amount as required and creates a barter event row
        """
        account = self.get_object()
        amount = float(request.data.get('amount', 0))

        try:
            if event_type == 'Add':
                account.add(amount)
            elif event_type in ['Buy_meal', 'Buy_card']:
                account.subtract(amount)
            else:
                """This SHOULD be unreachable. But just in case..."""
                return Response(
                    status=HTTP_400_BAD_REQUEST,
                    data={'result': 'unknown_action', 'message': f'Event type {event_type} is unknown'}
                )
        except BalanceLimitError as error:
            return Response(status=HTTP_400_BAD_REQUEST, data={'result': 'limit_error', 'message': f'{error}'})
        except AmountInputError as error:
            return Response(status=HTTP_400_BAD_REQUEST, data={'result': 'input_error', 'message': f'{error}'})

        return Response(status=HTTP_200_OK, data={'balance': account.balance.amount})

    # Adds /accounts/<pk>/credit endpoint
    @action(detail=True, methods=['post'], name='Add Credit')
    def credit(self, request, pk):
        response = self.update_balance_and_add_event(request, pk, 'Add')
        return response

    # Adds /accounts/<pk>/buy_meal endpoint
    @action(detail=True, methods=['post'], name='Buy Meal')
    def buy_meal(self, request, pk):
        response = self.update_balance_and_add_event(request, pk, 'Buy_meal')
        return response

    # Adds /accounts/<pk>/buy_card endpoint
    @action(detail=True, methods=['post'], name='Buy Card')
    def buy_card(self, request, pk):
        response = self.update_balance_and_add_event(request, pk, 'Buy_card')
        return response
