from __future__ import absolute_import
from django.urls import path, re_path

from . import views

urlpatterns = [
    re_path(r'^remove/(?P<obj_type>\S+)/(?P<obj_id>\S+)/$', views.remove_comment, name='crits-comments-views-remove_comment'),
    re_path(r'^(?P<method>\S+)/(?P<obj_type>\S+)/(?P<obj_id>\S+)/$', views.add_update_comment, name='crits-comments-views-add_update_comment'),
    re_path(r'^activity/$', views.activity, name='crits-comments-views-activity'),
    re_path(r'^activity/(?P<atype>\S+)/(?P<value>\S+)/$', views.activity, name='crits-comments-views-activity'),
    re_path(r'^activity/get_new_comments/$', views.get_new_comments, name='crits-comments-views-get_new_comments'),
    re_path(r'^search/(?P<stype>[A-Za-z0-9\-\._]+)/(?P<sterm>.+?)/$', views.comment_search, name='crits-comments-views-comment_search'),
    re_path(r'^list/$', views.comments_listing, name='crits-comments-views-comments_listing'),
    re_path(r'^list/(?P<option>\S+)/$', views.comments_listing, name='crits-comments-views-comments_listing'),
]
