from __future__ import absolute_import
from django.urls import path, re_path

from . import views

urlpatterns = [
    re_path(r'^$', views.events_listing, name='crits-events-views-events_listing_root'),
    re_path(r'^details/(?P<eventid>\w+)/$', views.view_event, name='crits-events-views-view_event'),
    re_path(r'^add/$', views.add_event, name='crits-events-views-add_event'),
    re_path(r'^search/$', views.event_search, name='crits-events-views-event_search'),
    re_path(r'^remove/(?P<_id>[\S ]+)$', views.remove_event, name='crits-events-views-remove_event'),
    re_path(r'^set_title/(?P<event_id>\w+)/$', views.set_event_title, name='crits-events-views-set_event_title'),
    re_path(r'^set_type/(?P<event_id>\w+)/$', views.set_event_type, name='crits-events-views-set_event_type'),
    re_path(r'^get_event_types/$', views.get_event_type_dropdown, name='crits-events-views-get_event_type_dropdown'),
    re_path(r'^list/$', views.events_listing, name='crits-events-views-events_listing'),
    re_path(r'^list/(?P<option>\S+)/$', views.events_listing, name='crits-events-views-events_listing'),
]
