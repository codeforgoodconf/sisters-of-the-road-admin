from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),

    url(r'^account/(?P<account_id>[0-9]+)/add$', views.account_add, name='account_add'),
    url(r'^account/subtract$', views.account_subtract, name='account_subtract'),

    url(r'^api/hello$', views.hello_api, name='hello_api')
]