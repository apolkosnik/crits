from __future__ import absolute_import
from django.urls import path, re_path

from . import views

urlpatterns = [
    re_path(r'^list/$', views.domains_listing, name='crits-domains-views-domains_listing'),
    re_path(r'^list/(?P<option>\S+)/$', views.domains_listing, name='crits-domains-views-domains_listing'),
    re_path(r'^tld_update/$', views.tld_update, name='crits-domains-views-tld_update'),
    re_path(r'^details/(?P<domain>\S+)/$', views.domain_detail, name='crits-domains-views-domain_detail'),
    re_path(r'^search/$', views.domain_search, name='crits-domains-views-domain_search'),
    re_path(r'^add/$', views.add_domain, name='crits-domains-views-add_domain'),
    re_path(r'^bulkadd/$', views.bulk_add_domain, name='crits-domains-views-bulk_add_domain'),
    re_path(r'^edit/(?P<domain>\S+)/$', views.edit_domain, name='crits-domains-views-edit_domain'),
]
