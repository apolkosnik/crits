from __future__ import absolute_import
from django.urls import path, re_path

from . import views

urlpatterns = [
    re_path(r'^list/$', views.targets_listing, name='crits-targets-views-targets_listing'),
    re_path(r'^list/(?P<option>\S+)/$', views.targets_listing, name='crits-targets-views-targets_listing'),
    re_path(r'^divisions/list/$', views.divisions_listing, name='crits-targets-views-divisions_listing'),
    re_path(r'^divisions/list/(?P<option>\S+)/$', views.divisions_listing, name='crits-targets-views-divisions_listing'),
    re_path(r'^add_target/$', views.add_update_target, name='crits-targets-views-add_update_target'),
    re_path(r'^details/(?P<email_address>[\S ]+)/$', views.target_details, name='crits-targets-views-target_details'),
    re_path(r'^details/$', views.target_details, name='crits-targets-views-target_details'),
    re_path(r'^info/(?P<email_address>[\S ]+)/$', views.target_info, name='crits-targets-views-target_info'),
]
