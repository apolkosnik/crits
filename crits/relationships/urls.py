from __future__ import absolute_import
from django.urls import path, re_path

from . import views

urlpatterns = [
    re_path(r'^forge/$', views.add_new_relationship, name='crits-relationships-views-add_new_relationship'),
    re_path(r'^breakup/$', views.break_relationship, name='crits-relationships-views-break_relationship'),
    re_path(r'^get_dropdown/$', views.get_relationship_type_dropdown, name='crits-relationships-views-get_relationship_type_dropdown'),
    re_path(r'^update_relationship_confidence/$', views.update_relationship_confidence, name='crits-relationships-views-update_relationship_confidence'),
    re_path(r'^update_relationship_reason/$', views.update_relationship_reason, name='crits-relationships-views-update_relationship_reason'),
    re_path(r'^update_relationship_type/$', views.update_relationship_type, name='crits-relationships-views-update_relationship_type'),
    re_path(r'^update_relationship_date/$', views.update_relationship_date, name='crits-relationships-views-update_relationship_date'),
]
