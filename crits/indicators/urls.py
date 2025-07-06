from __future__ import absolute_import
from django.urls import path, re_path

from . import views

urlpatterns = [
    re_path(r'^$', views.indicators_listing, name='crits-indicators-views-indicators_listing_root'),
    re_path(r'^details/(?P<indicator_id>\w+)/$', views.indicator, name='crits-indicators-views-indicator'),
    re_path(r'^search/$', views.indicator_search, name='crits-indicators-views-indicator_search'),
    re_path(r'^upload/$', views.upload_indicator, name='crits-indicators-views-upload_indicator'),
    re_path(r'^remove/(?P<_id>[\S ]+)$', views.remove_indicator, name='crits-indicators-views-remove_indicator'),
    re_path(r'^activity/remove/(?P<indicator_id>\w+)/$', views.remove_activity, name='crits-indicators-views-remove_activity'),
    re_path(r'^activity/(?P<method>\S+)/(?P<indicator_id>\w+)/$', views.add_update_activity, name='crits-indicators-views-add_update_activity'),
    re_path(r'^ci/update/(?P<indicator_id>\w+)/(?P<ci_type>\S+)/$', views.update_ci, name='crits-indicators-views-update_ci'),
    re_path(r'^type/update/(?P<indicator_id>\w+)/$', views.update_indicator_type, name='crits-indicators-views-update_indicator_type'),
    re_path(r'^threat_type/update/(?P<indicator_id>\w+)/$', views.threat_type_modify, name='crits-indicators-views-threat_type_modify'),
    re_path(r'^attack_type/update/(?P<indicator_id>\w+)/$', views.attack_type_modify, name='crits-indicators-views-attack_type_modify'),
    re_path(r'^and_ip/$', views.indicator_and_ip, name='crits-indicators-views-indicator_and_ip'),
    re_path(r'^from_obj/$', views.indicator_from_tlo, name='crits-indicators-views-indicator_from_tlo'),
    re_path(r'^list/$', views.indicators_listing, name='crits-indicators-views-indicators_listing'),
    re_path(r'^list/(?P<option>\S+)/$', views.indicators_listing, name='crits-indicators-views-indicators_listing'),
    re_path(r'^get_dropdown/$', views.get_indicator_type_dropdown, name='crits-indicators-views-get_indicator_type_dropdown'),
    re_path(r'^get_threat_types/$', views.get_available_threat_types, name='crits-indicators-views-get_available_threat_types'),
    re_path(r'^get_attack_types/$', views.get_available_attack_types, name='crits-indicators-views-get_available_attack_types'),
]
