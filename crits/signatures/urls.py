from __future__ import absolute_import
from django.urls import path, re_path

from . import views

urlpatterns = [
    re_path(r'^details/(?P<_id>\w+)/$', views.signature_detail, name='crits-signatures-views-signature_detail'),
    re_path(r'^details_by_link/(?P<link>.+)/$', views.details_by_link, name='crits-signatures-views-details_by_link'),
    re_path(r'^get_versions/(?P<_id>\w+)/$', views.get_signature_versions, name='crits-signatures-views-get_signature_versions'),
    re_path(r'^set_signature_type/(?P<id_>\w+)/$', views.set_signature_type, name='crits-signatures-views-set_signature_type'),
    re_path(r'^update_data_type_min_version/$', views.update_data_type_min_version, name='crits-signatures-views-update_data_type_min_version'),
    re_path(r'^update_data_type_max_version/$', views.update_data_type_max_version, name='crits-signatures-views-update_data_type_max_version'),
    re_path(r'^update_data_type_dependency/$', views.update_data_type_dependency, name='crits-signatures-views-update_data_type_dependency'),
    re_path(r'^upload/(?P<link_id>.+)/$', views.upload_signature, name='crits-signatures-views-upload_signature'),
    re_path(r'^upload/$', views.upload_signature, name='crits-signatures-views-upload_signature'),
    re_path(r'^remove/(?P<_id>[\S ]+)$', views.remove_signature, name='crits-signatures-views-remove_signature'),
    re_path(r'^list/$', views.signatures_listing, name='crits-signatures-views-signatures_listing'),
    re_path(r'^list/(?P<option>\S+)/$', views.signatures_listing, name='crits-signatures-views-signatures_listing'),
    re_path(r'^add_data_type/$', views.new_signature_type, name='crits-signatures-views-new_signature_type'),
    re_path(r'^add_data_dependency/$', views.new_signature_dependency, name='crits-signatures-views-new_signature_dependency'),
    re_path(r'^get_data_types/$', views.get_signature_type_dropdown, name='crits-signatures-views-get_signature_type_dropdown'),
    re_path(r'^signatures/autocomplete/$', views.dependency_autocomplete, name='crits-signatures-views-dependency_autocomplete'),
    re_path(r'^remove_signature_dependency/$', views.remove_signature_dependency, name='crits-signatures-views-remove_signature_dependency'),
]
