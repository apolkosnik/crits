from __future__ import absolute_import
from django.urls import path, re_path

from . import views

urlpatterns = [
    re_path(r'^search/$', views.email_search, name='crits-emails-views-email_search'),
    re_path(r'^delete/(?P<email_id>\w+)/$', views.email_del, name='crits-emails-views-email_del'),
    re_path(r'^upload/attach/(?P<email_id>\w+)/$', views.upload_attach, name='crits-emails-views-upload_attach'),
    re_path(r'^details/(?P<email_id>\w+)/$', views.email_detail, name='crits-emails-views-email_detail'),
    re_path(r'^new/fields/$', views.email_fields_add, name='crits-emails-views-email_fields_add'),
    re_path(r'^new/outlook/$', views.email_outlook_add, name='crits-emails-views-email_outlook_add'),
    re_path(r'^new/raw/$', views.email_raw_add, name='crits-emails-views-email_raw_add'),
    re_path(r'^new/yaml/$', views.email_yaml_add, name='crits-emails-views-email_yaml_add'),
    re_path(r'^new/eml/$', views.email_eml_add, name='crits-emails-views-email_eml_add'),
    re_path(r'^edit/(?P<email_id>\w+)/$', views.email_yaml_add, name='crits-emails-views-email_yaml_add'),
    re_path(r'^update_header_value/(?P<email_id>\w+)/$', views.update_header_value, name='crits-emails-views-update_header_value'),
    re_path(r'^indicator_from_header_field/(?P<email_id>\w+)/$', views.indicator_from_header_field, name='crits-emails-views-indicator_from_header_field'),
    re_path(r'^list/$', views.emails_listing, name='crits-emails-views-emails_listing'),
    re_path(r'^list/(?P<option>\S+)/$', views.emails_listing, name='crits-emails-views-emails_listing'),
]
