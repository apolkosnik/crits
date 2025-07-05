from __future__ import absolute_import
from django.urls import path, re_path

from . import views

urlpatterns = [
    re_path(r'^add/$', views.add_backdoor, name='crits-backdoors-views-add_backdoor'),
    re_path(r'^edit/aliases/$', views.edit_backdoor_aliases, name='crits-backdoors-views-edit_backdoor_aliases'),
    re_path(r'^edit/name/(?P<id_>\S+)/$', views.edit_backdoor_name, name='crits-backdoors-views-edit_backdoor_name'),
    re_path(r'^edit/version/(?P<id_>\S+)/$', views.edit_backdoor_version, name='crits-backdoors-views-edit_backdoor_version'),
    re_path(r'^details/(?P<id_>\S+)/$', views.backdoor_detail, name='crits-backdoors-views-backdoor_detail'),
    re_path(r'^remove/(?P<id_>\S+)/$', views.remove_backdoor, name='crits-backdoors-views-remove_backdoor'),
    re_path(r'^list/$', views.backdoors_listing, name='crits-backdoors-views-backdoors_listing'),
    re_path(r'^list/(?P<option>\S+)/$', views.backdoors_listing, name='crits-backdoors-views-backdoors_listing'),
]
