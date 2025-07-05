from __future__ import absolute_import
from django.urls import path, re_path

from . import views

urlpatterns = [
    re_path(r'^add/$', views.add_new_object, name='crits-objects-views-add_new_object'),
    re_path(r'^delete/$', views.delete_this_object, name='crits-objects-views-delete_this_object'),
    re_path(r'^get_dropdown/$', views.get_object_type_dropdown, name='crits-objects-views-get_object_type_dropdown'),
    re_path(r'^update_objects_value/$', views.update_objects_value, name='crits-objects-views-update_objects_value'),
    re_path(r'^update_objects_source/$', views.update_objects_source, name='crits-objects-views-update_objects_source'),
    re_path(r'^create_indicator/$', views.indicator_from_object, name='crits-objects-views-indicator_from_object'),
    re_path(r'^bulkadd/$', views.bulk_add_object, name='crits-objects-views-bulk_add_object'),
    re_path(r'^bulkaddinline/$', views.bulk_add_object_inline, name='crits-objects-views-bulk_add_object_inline'),
]
