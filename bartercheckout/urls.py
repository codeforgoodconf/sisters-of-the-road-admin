from django.conf.urls import url
from django.urls import include
from rest_framework.routers import DefaultRouter

from bartercheckout.views import barter_account, barter_event

router = DefaultRouter(trailing_slash=False)

router.register(r'accounts', viewset=barter_account.BarterAccountViewSet, basename='accounts')
router.register(
    r'accounts/(?P<account_id>\d+)/events', viewset=barter_event.BarterEventViewSet, basename='events'
)

urlpatterns = [
    url(r'^', include(router.urls)),
]
