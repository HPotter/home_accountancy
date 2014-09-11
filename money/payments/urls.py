from django.conf.urls import url

from . import views

urlpatterns = [
    url('^$', views.my_payments, name='my_payments'),
    url('^all/$', views.payments, name='payments'),
]