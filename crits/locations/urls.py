from __future__ import absolute_import
from django.urls import path, re_path

from . import views

urlpatterns = [
    re_path(r'^add/(?P<type_>\w+)/(?P<id_>\w+)/$', views.add_location, name='crits-locations-views-add_location'),
    re_path(r'^edit/(?P<type_>\w+)/(?P<id_>\w+)/$', views.edit_location, name='crits-locations-views-edit_location'),
    re_path(r'^remove/(?P<type_>\w+)/(?P<id_>\w+)/$', views.remove_location, name='crits-locations-views-remove_location'),
    re_path(r'^name_list/$', views.location_names, name='crits-locations-views-location_names'),
    re_path(r'^name_list/(?P<active_only>\S+)/$', views.location_names, name='crits-locations-views-location_names'),
]
