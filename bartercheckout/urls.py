from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),

    url(r'^account/(?P<account_id>[0-9]+)/add$', views.add, name='add'),
    url(r'^account/(?P<account_id>[0-9]+)/subtract$', views.subtract, name='subtract'),

    url(r'^api/hello$', views.hello_api, name='hello_api')

]