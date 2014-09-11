from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'payments/', include('payments.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
