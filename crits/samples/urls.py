from __future__ import absolute_import
from django.urls import path, re_path

from . import views

urlpatterns = [
        re_path(r'^$', views.samples_listing, name='crits-samples-views-samples_listing_root'),
        re_path(r'^upload/$', views.upload_file, name='crits-samples-views-upload_file'),
        re_path(r'^upload/(?P<related_md5>\w+)/$', views.upload_file, name='crits-samples-views-upload_file'),
        re_path(r'^upload_list/(?P<filename>[\S ]+)/(?P<md5s>.+)/$', views.view_upload_list, name='crits-samples-views-view_upload_list'),
        re_path(r'^bulkadd/$', views.bulk_add_md5_sample, name='crits-samples-views-bulk_add_md5_sample'),
        re_path(r'^details/(?P<sample_md5>\w+)/$', views.detail, name='crits-samples-views-detail'),
        re_path(r'^strings/(?P<sample_md5>\w+)/$', views.strings, name='crits-samples-views-strings'),
        re_path(r'^stackstrings/(?P<sample_md5>\w+)/$', views.stackstrings, name='crits-samples-views-stackstrings'),
        re_path(r'^hex/(?P<sample_md5>\w+)/$', views.hex, name='crits-samples-views-hex'),
        re_path(r'^xor/(?P<sample_md5>\w+)/$', views.xor, name='crits-samples-views-xor'),
        re_path(r'^xor_searcher/(?P<sample_md5>\w+)/$', views.xor_searcher, name='crits-samples-views-xor_searcher'),
        re_path(r'^unzip/(?P<md5>\w+)/$', views.unzip_sample, name='crits-samples-views-unzip_sample'),
        re_path(r'^sources/$', views.sources, name='crits-samples-views-sources'),
        re_path(r'^remove/(?P<md5>[\S ]+)$', views.remove_sample, name='crits-samples-views-remove_sample'),
        re_path(r'^list/$', views.samples_listing, name='crits-samples-views-samples_listing'),
        re_path(r'^list/(?P<option>\S+)/$', views.samples_listing, name='crits-samples-views-samples_listing'),
        re_path(r'^yarahits/list/$', views.yarahits_listing, name='crits-samples-views-yarahits_listing'),
        re_path(r'^yarahits/list/(?P<option>\S+)/$', views.yarahits_listing, name='crits-samples-views-yarahits_listing'),
        re_path(r'^set_filename/$', views.set_sample_filename, name='crits-samples-views-set_sample_filename'),
        re_path(r'^filenames/$', views.set_sample_filenames, name='crits-samples-views-set_sample_filenames'),
]
