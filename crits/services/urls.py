from __future__ import absolute_import
import os

from django.conf import settings
from django.conf.urls import include, url

from . import views

urlpatterns = [
    re_path(r'^list/$', views.list, name='crits-services-views-list'),
    re_path(r'^analysis_results/list/$', views.analysis_results_listing, name='crits-services-views-analysis_results_listing'),
    re_path(r'^analysis_results/list/(?P<option>\S+)/$', views.analysis_results_listing, name='crits-services-views-analysis_results_listing'),
    re_path(r'^analysis_results/details/(?P<analysis_id>\w+)/$', views.analysis_result, name='crits-services-views-analysis_result'),
    re_path(r'^detail/(?P<name>[\w ]+)/$', views.detail, name='crits-services-views-detail'),
    re_path(r'^enable/(?P<name>[\w ]+)/$', views.enable, name='crits-services-views-enable'),
    re_path(r'^disable/(?P<name>[\w ]+)/$', views.disable, name='crits-services-views-disable'),
    re_path(r'^enable_triage/(?P<name>[\w ]+)/$', views.enable_triage, name='crits-services-views-enable_triage'),
    re_path(r'^disable_triage/(?P<name>[\w ]+)/$', views.disable_triage, name='crits-services-views-disable_triage'),
    re_path(r'^edit/(?P<name>[\w ]+)/$', views.edit_config, name='crits-services-views-edit_config'),
    re_path(r'^refresh/(?P<crits_type>\w+)/(?P<identifier>\w+)/$', views.refresh_services, name='crits-services-views-refresh_services'),
    re_path(r'^form/(?P<name>[\w ]+)/(?P<crits_type>\w+)/(?P<identifier>\w+)/$', views.get_form, name='crits-services-views-get_form'),
    re_path(r'^run/(?P<name>[\w ]+)/(?P<crits_type>\w+)/(?P<identifier>\w+)/$', views.service_run, name='crits-services-views-service_run'),
    re_path(r'^delete_task/(?P<crits_type>\w+)/(?P<identifier>\w+)/(?P<task_id>[-\w]+)/$', views.delete_task, name='crits-services-views-delete_task'),
]

for service_directory in settings.SERVICE_DIRS:
    if os.path.isdir(service_directory):
        for d in os.listdir(service_directory):
            abs_path = os.path.join(service_directory, d, 'urls.py')
            if os.path.isfile(abs_path):
                urlpatterns.append(
                    re_path(r'^%s/' % d, include('%s.urls' % d)))
