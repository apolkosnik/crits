from __future__ import absolute_import
from django.urls import path, re_path

from . import views

# Dashboard
urlpatterns = [
    re_path(r'^new_saved_search/$', views.new_save_search, name='crits-dashboards-views-new_save_search'),
    re_path(r'^$', views.dashboard, name='crits-dashboards-views-dashboard'),
    re_path(r'^id/(?P<dashId>\w+)/$', views.dashboard, name='crits-dashboards-views-dashboard'),
    re_path(r'^edit_saved_search/(?P<id>\S+)/$', views.edit_save_search, name='crits-dashboards-views-edit_save_search'),
    re_path(r'^delete_save_search/$', views.delete_save_search, name='crits-dashboards-views-delete_save_search'),
    re_path(r'^load_data/(?P<obj>\w+)/$', views.load_data, name='crits-dashboards-views-load_data'),
    re_path(r'^load_data/(?P<obj>\w+)/(?P<term>\w+)/$', views.load_data, name='crits-dashboards-views-load_data'),
    re_path(r'^save_search/$', views.save_search, name='crits-dashboards-views-save_search'),
    re_path(r'^save_new_dashboard/$', views.save_new_dashboard, name='crits-dashboards-views-save_new_dashboard'),
    re_path(r'^destroy_dashboard/$', views.destroy_dashboard, name='crits-dashboards-views-destroy_dashboard'),
    re_path(r'^get_dashboard_table_data/(?P<tableName>\w+)/$', views.get_dashboard_table_data, name='crits-dashboards-views-get_dashboard_table_data'),
    re_path(r'^configurations/$', views.saved_searches_list, name='crits-dashboards-views-saved_searches_list'),
    re_path(r'^toggle_table_visibility/$', views.toggle_table_visibility, name='crits-dashboards-views-toggle_table_visibility'),
    re_path(r'^set_default_dashboard/$', views.set_default_dashboard, name='crits-dashboards-views-set_default_dashboard'),
    re_path(r'^set_dashboard_public/$', views.set_dashboard_public, name='crits-dashboards-views-set_dashboard_public'),
    re_path(r'^ignore_parent/(?P<id>\S+)/$', views.ignore_parent, name='crits-dashboards-views-ignore_parent'),
    re_path(r'^delete_dashboard/$', views.delete_dashboard, name='crits-dashboards-views-delete_dashboard'),
    re_path(r'^rename_dashboard/$', views.rename_dashboard, name='crits-dashboards-views-rename_dashboard'),
    re_path(r'^change_theme/$', views.change_theme, name='crits-dashboards-views-change_theme'),
    re_path(r'^create_blank_dashboard/$', views.create_blank_dashboard, name='crits-dashboards-views-create_blank_dashboard'),
    re_path(r'^add_search/$', views.add_search, name='crits-dashboards-views-add_search'),
    re_path(r'^switch_dashboard/$', views.switch_dashboard, name='crits-dashboards-views-switch_dashboard'),
]
