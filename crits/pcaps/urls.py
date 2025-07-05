from __future__ import absolute_import
from django.urls import path, re_path

from . import views

urlpatterns = [
    re_path(r'^details/(?P<md5>\w+)/$', views.pcap_details, name='crits-pcaps-views-pcap_details'),
    re_path(r'^upload/$', views.upload_pcap, name='crits-pcaps-views-upload_pcap'),
    re_path(r'^remove/(?P<md5>[\S ]+)$', views.remove_pcap, name='crits-pcaps-views-remove_pcap'),
    re_path(r'^list/$', views.pcaps_listing, name='crits-pcaps-views-pcaps_listing'),
    re_path(r'^list/(?P<option>\S+)/$', views.pcaps_listing, name='crits-pcaps-views-pcaps_listing'),
]
