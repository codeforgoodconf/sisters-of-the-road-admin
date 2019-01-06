import rest_framework_filters as filters
from rest_framework import serializers, viewsets

from bartercheckout.models import BarterAccount, BarterEvent


class BarterEventFilter(filters.FilterSet):
    class Meta:
        model = BarterEvent
        fields = {
            'barter_account': '__all__',
            'event_time': '__all__',
            'amount': '__all__',
        }

    account = filters.RelatedFilter('BarterAccountFilter', queryset=BarterAccount.objects.all())


class BarterEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = BarterEvent
        fields = ['barter_account', 'event_time', 'amount']


class BarterEventViewSet(viewsets.ModelViewSet):
    queryset = BarterEvent.objects.all()
    serializer_class = BarterEventSerializer
    filter_class = BarterEventFilter
    lookup_field = 'pk'
    lookup_url_kwarg = 'event_id'
