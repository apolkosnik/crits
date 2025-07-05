from __future__ import absolute_import
from django.urls import path, re_path

from . import views

urlpatterns = [
    re_path(r'^details/(?P<_id>\w+)/$', views.raw_data_details, name='crits-raw_data-views-raw_data_details'),
    re_path(r'^details_by_link/(?P<link>.+)/$', views.details_by_link, name='crits-raw_data-views-details_by_link'),
    re_path(r'^get_inline_comments/(?P<_id>\w+)/$', views.get_inline_comments, name='crits-raw_data-views-get_inline_comments'),
    re_path(r'^get_versions/(?P<_id>\w+)/$', views.get_raw_data_versions, name='crits-raw_data-views-get_raw_data_versions'),
    re_path(r'^set_tool_details/(?P<_id>\w+)/$', views.set_raw_data_tool_details, name='crits-raw_data-views-set_raw_data_tool_details'),
    re_path(r'^set_tool_name/(?P<_id>\w+)/$', views.set_raw_data_tool_name, name='crits-raw_data-views-set_raw_data_tool_name'),
    re_path(r'^set_raw_data_type/(?P<_id>\w+)/$', views.set_raw_data_type, name='crits-raw_data-views-set_raw_data_type'),
    re_path(r'^set_raw_data_highlight_comment/(?P<_id>\w+)/$', views.set_raw_data_highlight_comment, name='crits-raw_data-views-set_raw_data_highlight_comment'),
    re_path(r'^set_raw_data_highlight_date/(?P<_id>\w+)/$', views.set_raw_data_highlight_date, name='crits-raw_data-views-set_raw_data_highlight_date'),
    re_path(r'^add_inline_comment/(?P<_id>\w+)/$', views.add_inline_comment, name='crits-raw_data-views-add_inline_comment'),
    re_path(r'^add_highlight/(?P<_id>\w+)/$', views.add_highlight, name='crits-raw_data-views-add_highlight'),
    re_path(r'^remove_highlight/(?P<_id>\w+)/$', views.remove_highlight, name='crits-raw_data-views-remove_highlight'),
    re_path(r'^upload/(?P<link_id>.+)/$', views.upload_raw_data, name='crits-raw_data-views-upload_raw_data'),
    re_path(r'^upload/$', views.upload_raw_data, name='crits-raw_data-views-upload_raw_data'),
    re_path(r'^remove/(?P<_id>[\S ]+)$', views.remove_raw_data, name='crits-raw_data-views-remove_raw_data'),
    re_path(r'^list/$', views.raw_data_listing, name='crits-raw_data-views-raw_data_listing'),
    re_path(r'^list/(?P<option>\S+)/$', views.raw_data_listing, name='crits-raw_data-views-raw_data_listing'),
    re_path(r'^add_data_type/$', views.new_raw_data_type, name='crits-raw_data-views-new_raw_data_type'),
    re_path(r'^get_data_types/$', views.get_raw_data_type_dropdown, name='crits-raw_data-views-get_raw_data_type_dropdown'),
]
