# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
]

if 'mysite.apps.apptest' in settings.INSTALLED_APPS:  # pragma: nobranch
    urlpatterns += [
        url(r'^', include('mysite.apps.apptest.urls', namespace='apptest')),
    ]

admin.site.site_header = 'mysite'
