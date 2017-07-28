from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^account/', views.account, name='account'),
    url(r'^buymeal/', views.buymeal, name='buymeal'),
    url(r'^addcredit/', views.addcredit, name='addcredit')
]