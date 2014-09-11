from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import RedirectView

urlpatterns = patterns('',
    url(r'^$', RedirectView.as_view(pattern_name='payments')),
    url(r'payments/', include('payments.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
