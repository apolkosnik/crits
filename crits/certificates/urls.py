from __future__ import absolute_import
from django.urls import path, re_path

from . import views

urlpatterns = [
    re_path(r'^details/(?P<md5>\w+)/$', views.certificate_details, name='crits-certificates-views-certificate_details'),
    re_path(r'^upload/$', views.upload_certificate, name='crits-certificates-views-upload_certificate'),
    re_path(r'^remove/(?P<md5>[\S ]+)$', views.remove_certificate, name='crits-certificates-views-remove_certificate'),
    re_path(r'^list/$', views.certificates_listing, name='crits-certificates-views-certificates_listing'),
    re_path(r'^list/(?P<option>\S+)/$', views.certificates_listing, name='crits-certificates-views-certificates_listing'),
]
