import rest_framework_filters as filters
from rest_framework import serializers, viewsets

from bartercheckout.models import BarterAccount, BarterEvent
from bartercheckout.views import BarterAccountFilter


class BarterEventFilter(filters.FilterSet):
    class Meta:
        model = BarterEvent
        fields = {
            'event_type': '__all__',
            'barter_account': '__all__',
            'event_time': '__all__',
            'amount': '__all__',
        }

    account = filters.RelatedFilter(BarterAccountFilter, queryset=BarterAccount.objects.all())


class BarterEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = BarterEvent
        fields = ['event_type', 'barter_account', 'event_time', 'amount']


class BarterEventViewSet(viewsets.ModelViewSet):
    serializer_class = BarterEventSerializer
    filter_class = BarterEventFilter
    lookup_field = 'pk'
    lookup_url_kwarg = 'event_id'

    def get_queryset(self):
        return BarterEvent.objects.filter(barter_account=self.kwargs['account_id'])
