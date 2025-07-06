from __future__ import absolute_import
from django.urls import path, re_path

from . import views

urlpatterns = [
    re_path(r'^$', views.campaigns_listing, name='crits-campaigns-views-campaigns_listing_root'),
    re_path(r'^stats/$', views.campaign_stats, name='crits-campaigns-views-campaign_stats'),
    re_path(r'^name_list/$', views.campaign_names, name='crits-campaigns-views-campaign_names'),
    re_path(r'^name_list/(?P<active_only>\S+)/$', views.campaign_names, name='crits-campaigns-views-campaign_names'),
    re_path(r'^list/$', views.campaigns_listing, name='crits-campaigns-views-campaigns_listing'),
    re_path(r'^list/(?P<option>\S+)/$', views.campaigns_listing, name='crits-campaigns-views-campaigns_listing'),
    re_path(r'^details/(?P<campaign_name>.+?)/$', views.campaign_details, name='crits-campaigns-views-campaign_details'),
    re_path(r'^add/(?P<ctype>\w+)/(?P<objectid>\w+)/$', views.campaign_add, name='crits-campaigns-views-campaign_add'),
    re_path(r'^new/$', views.add_campaign, name='crits-campaigns-views-add_campaign'),
    re_path(r'^remove/(?P<ctype>\w+)/(?P<objectid>\w+)/$', views.remove_campaign, name='crits-campaigns-views-remove_campaign'),
    re_path(r'^edit/(?P<ctype>\w+)/(?P<objectid>\w+)/$', views.edit_campaign, name='crits-campaigns-views-edit_campaign'),
    re_path(r'^ttp/(?P<cid>\w+)/$', views.campaign_ttp, name='crits-campaigns-views-campaign_ttp'),
    re_path(r'^aliases/$', views.campaign_aliases, name='crits-campaigns-views-campaign_aliases'),
]
