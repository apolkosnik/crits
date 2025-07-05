from __future__ import absolute_import
from django.urls import path, re_path

from . import views

urlpatterns = [
    re_path(r'^poll/$', views.poll, name='crits-notifications-views-poll'),
    re_path(r'^ack/$', views.acknowledge, name='crits-notifications-views-acknowledge'),
]
