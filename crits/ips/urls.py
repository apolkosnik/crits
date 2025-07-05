from __future__ import absolute_import
from django.urls import path, re_path

from . import views

urlpatterns = [
    re_path(r'^search/$', views.ip_search, name='crits-ips-views-ip_search'),
    re_path(r'^search/(?P<ip_str>\S+)/$', views.ip_search, name='crits-ips-views-ip_search'),
    re_path(r'^details/(?P<ip>\S+)/$', views.ip_detail, name='crits-ips-views-ip_detail'),
    re_path(r'^remove/$', views.remove_ip, name='crits-ips-views-remove_ip'),
    re_path(r'^list/$', views.ips_listing, name='crits-ips-views-ips_listing'),
    re_path(r'^list/(?P<option>\S+)/$', views.ips_listing, name='crits-ips-views-ips_listing'),
    re_path(r'^bulkadd/$', views.bulk_add_ip, name='crits-ips-views-bulk_add_ip'),
    re_path(r'^(?P<method>\S+)/$', views.add_update_ip, name='crits-ips-views-add_update_ip'),
]
