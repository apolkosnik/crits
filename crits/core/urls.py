from __future__ import absolute_import
from django.urls import path, re_path
from django.contrib.auth.views import logout_then_login

from . import views

from crits.config import views as cviews
# crits_config, modify_config
from crits.dashboards import views as dviews

urlpatterns = [

    # Authentication
    path('login/', views.login, name='crits-core-views-login'),
    path('logout/', logout_then_login, name='crits-core-views-logout_then_login'),

    # Buckets
    path('bucket/list/', views.bucket_list, name='crits-core-views-bucket_list'),
    re_path(r'^bucket/list/(?P<option>.+)$', views.bucket_list, name='crits-core-views-bucket_list'),
    path('bucket/mod/', views.bucket_modify, name='crits-core-views-bucket_modify'),
    path('bucket/autocomplete/', views.bucket_autocomplete, name='crits-core-views-bucket_autocomplete'),
    path('bucket/promote/', views.bucket_promote, name='crits-core-views-bucket_promote'),

    # Common functionality for all TLOs
    re_path(r'^status/update/(?P<type_>\S+)/(?P<id_>\S+)/$', views.update_status, name='crits-core-views-update_status'),
    re_path(r'^search/$', views.global_search_listing, name='crits-core-views-global_search_listing'),
    re_path(r'^object/download/$', views.download_object, name='crits-core-views-download_object'),
    re_path(r'^files/download/(?P<sample_md5>\w+)/$', views.download_file, name='crits-core-views-download_file'),
    re_path(r'^object/sources/removeall/(?P<obj_type>\S+)/(?P<obj_id>\S+)/$', views.remove_all_source, name='crits-core-views-remove_all_source'),
    re_path(r'^object/sources/remove/(?P<obj_type>\S+)/(?P<obj_id>\S+)/$', views.remove_source, name='crits-core-views-remove_source'),
    re_path(r'^object/sources/(?P<method>\S+)/(?P<obj_type>\S+)/(?P<obj_id>\S+)/$', views.add_update_source, name='crits-core-views-add_update_source'),
    re_path(r'^source_releasability/$', views.source_releasability, name='crits-core-views-source_releasability'),
    re_path(r'^tickets/(?P<method>\S+)/(?P<type_>\w+)/(?P<id_>\w+)/$', views.add_update_ticket, name='crits-core-views-add_update_ticket'),
    re_path(r'^preferred_actions/$', views.add_preferred_actions, name='crits-core-views-add_preferred_actions'),
    re_path(r'^actions/(?P<method>\S+)/(?P<obj_type>\S+)/(?P<obj_id>\w+)/$', views.add_update_action, name='crits-core-views-add_update_action'),
    re_path(r'^action/remove/(?P<obj_type>\S+)/(?P<obj_id>\w+)/$', views.remove_action, name='crits-core-views-remove_action'),
    re_path(r'^add_action/$', views.new_action, name='crits-core-views-new_action'),
    re_path(r'^get_actions_for_tlo/$', views.get_actions_for_tlo, name='crits-core-views-get_actions_for_tlo'),


    # CRITs Configuration
    re_path(r'^config/$', cviews.crits_config, name='crits-config-views-crits_config'),
    re_path(r'^modify_config/$', cviews.modify_config, name='crits-config-views-modify_config'),
    re_path(r'^audit/list/$', views.audit_listing, name='crits-core-views-audit_listing'),
    re_path(r'^audit/list/(?P<option>\S+)/$', views.audit_listing, name='crits-core-views-audit_listing'),
    re_path(r'^items/editor/$', views.item_editor, name='crits-core-views-item_editor'),
    re_path(r'^items/list/$', views.items_listing, name='crits-core-views-items_listing'),
    re_path(r'^items/list/(?P<itype>\S+)/(?P<option>\S+)/$', views.items_listing, name='crits-core-views-items_listing'),
    re_path(r'^items/toggle_active/$', views.toggle_item_active, name='crits-core-views-toggle_item_active'),
    re_path(r'^users/toggle_active/$', views.toggle_user_active, name='crits-core-views-toggle_user_active'),
    re_path(r'^users/list/(?P<option>\S+)/$', views.users_listing, name='crits-core-views-users_listing'),
    re_path(r'^users/list/$', views.users_listing, name='crits-core-views-users_listing'),
    re_path(r'^roles/list/(?P<option>\S+)/$', views.roles_listing, name='crits-core-views-roles_listing'),
    re_path(r'^roles/list/$', views.roles_listing, name='crits-core-views-roles_listing'),
    re_path(r'^roles/add/$', views.role_add, name='crits-core-views-role_add'),
    re_path(r'^roles/details/(?P<rid>\S+)/$', views.role_details, name='crits-core-views-role_details'),
    re_path(r'^roles/details/$', views.role_details, name='crits-core-views-role_details'),
    re_path(r'^roles/update/$', views.role_value_change, name='crits-core-views-role_value_change'),
    re_path(r'^roles/graph/$', views.role_graph, name='crits-core-views-role_graph'),
    re_path(r'^roles/add_source/$', views.role_add_source, name='crits-core-views-role_add_source'),
    re_path(r'^roles/remove_source/$', views.role_remove_source, name='crits-core-views-role_remove_source'),
    re_path(r'^roles/update_name/$', views.update_role_name, name='crits-core-views-update_role_name'),
    re_path(r'^roles/update_description/$', views.update_role_description, name='crits-core-views-update_role_description'),
    re_path(r'^get_item_data/$', views.get_item_data, name='crits-core-views-get_item_data'),
    re_path(r'^add_action/$', views.new_action, name='crits-core-views-new_action'),


    # Default landing page
    re_path(r'^$', dviews.dashboard, name='crits-dashboards-views-dashboard'),
    re_path(r'^counts/list/$', views.counts_listing, name='crits-core-views-counts_listing'),
    re_path(r'^counts/list/(?P<option>\S+)/$', views.counts_listing, name='crits-core-views-counts_listing'),

    # Dialogs
    re_path(r'^get_dialog/(?P<dialog>[A-Za-z0-9\-\._-]+)$', views.get_dialog, name='crits-core-views-get_dialog'),
    re_path(r'^get_dialog/$', views.get_dialog, name='crits-core-views-get_dialog'),

    # General core pages
    re_path(r'^details/(?P<type_>\S+)/(?P<id_>\S+)/$', views.details, name='crits-core-views-details'),
    re_path(r'^update_object_description/', views.update_object_description, name='crits-core-views-update_object_description'),
    re_path(r'^update_object_data/', views.update_object_data, name='crits-core-views-update_object_data'),

    # Helper pages
    re_path(r'^about/$', views.about, name='crits-core-views-about'),
    re_path(r'^help/$', views.help, name='crits-core-views-help'),
    re_path(r'^get_search_help/$', views.get_search_help, name='crits-core-views-get_search_help'),

    # Sectors
    re_path(r'^sector/list/$', views.sector_list, name='crits-core-views-sector_list'),
    re_path(r'^sector/list/(?P<option>.+)$', views.sector_list, name='crits-core-views-sector_list'),
    re_path(r'^sector/mod/$', views.sector_modify, name='crits-core-views-sector_modify'),
    re_path(r'^sector/options/$', views.get_available_sectors, name='crits-core-views-get_available_sectors'),

    # Timeline
    re_path(r'^timeline/(?P<data_type>\S+)/$', views.timeline, name='crits-core-views-timeline'),
    re_path(r'^timeline/(?P<data_type>\S+)/(?P<extra_data>\S+)/$', views.timeline, name='crits-core-views-timeline'),
    re_path(r'^timeline/$', views.timeline, name='crits-core-views-timeline'),

    # TLP
    re_path(r'^tlp/mod/$', views.tlp_modify, name='crits-core-views-tlp_modify'),

    # User Stuff
    re_path(r'^profile/(?P<user>\S+)/$', views.profile, name='crits-core-views-profile'),
    re_path(r'^profile/$', views.profile, name='crits-core-views-profile'),
    re_path(r'^source_access/$', views.source_access, name='crits-core-views-source_access'),
    re_path(r'^source_add/$', views.source_add, name='crits-core-views-source_add'),
    re_path(r'^get_user_source_list/$', views.get_user_source_list, name='crits-core-views-get_user_source_list'),
    re_path(r'^user_source_access/$', views.user_source_access, name='crits-core-views-user_source_access'),
    re_path(r'^user_source_access/(?P<username>\S+)/$', views.user_source_access, name='crits-core-views-user_source_access'),
    re_path(r'^preference_toggle/(?P<section>\S+)/(?P<setting>\S+)/$', views.user_preference_toggle, name='crits-core-views-user_preference_toggle'),
    re_path(r'^preference_update/(?P<section>\S+)/$', views.user_preference_update, name='crits-core-views-user_preference_update'),
    re_path(r'^clear_user_notifications/$', views.clear_user_notifications, name='crits-core-views-clear_user_notifications'),
    re_path(r'^delete_user_notification/(?P<type_>\S+)/(?P<oid>\S+)/$', views.delete_user_notification, name='crits-core-views-delete_user_notification'),
    re_path(r'^change_subscription/(?P<stype>\S+)/(?P<oid>\S+)/$', views.change_subscription, name='crits-core-views-change_subscription'),
    re_path(r'^source_subscription/$', views.source_subscription, name='crits-core-views-source_subscription'),
    re_path(r'^change_password/$', views.change_password, name='crits-core-views-change_password'),
    re_path(r'^change_totp_pin/$', views.change_totp_pin, name='crits-core-views-change_totp_pin'),
    re_path(r'^reset_password/$', views.reset_password, name='crits-core-views-reset_password'),
    re_path(r'^favorites/toggle/$', views.toggle_favorite, name='crits-core-views-toggle_favorite'),
    re_path(r'^favorites/view/$', views.favorites, name='crits-core-views-favorites'),
    re_path(r'^favorites/list/(?P<ctype>\S+)/(?P<option>\S+)/$', views.favorites_list, name='crits-core-views-favorites_list'),

    # User API Authentication
    re_path(r'^get_api_key/$', views.get_api_key, name='crits-core-views-get_api_key'),
    re_path(r'^create_api_key/$', views.create_api_key, name='crits-core-views-create_api_key'),
    re_path(r'^make_default_api_key/$', views.make_default_api_key, name='crits-core-views-make_default_api_key'),
    re_path(r'^revoke_api_key/$', views.revoke_api_key, name='crits-core-views-revoke_api_key'),

]
