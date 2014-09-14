from django.conf.urls import url

from . import views
from django.views.generic.base import RedirectView

urlpatterns = [
    url(r'^$', RedirectView.as_view(pattern_name='payments')),

    url('^view/all/$', views.payments, name='payments'),
    url('^view/my/$', views.my_payments, name='my_payments'),

    url('^deal/([0-9]+)/$', views.deal_payment, name='deal_payment'),
]