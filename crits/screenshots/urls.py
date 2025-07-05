from __future__ import absolute_import
from django.urls import path, re_path

from . import views

urlpatterns = [
    re_path(r'^list/$', views.screenshots_listing, name='crits-screenshots-views-screenshots_listing'),
    re_path(r'^list/(?P<option>\S+)/$', views.screenshots_listing, name='crits-screenshots-views-screenshots_listing'),
    re_path(r'^add/$', views.add_new_screenshot, name='crits-screenshots-views-add_new_screenshot'),
    re_path(r'^find/$', views.find_screenshot, name='crits-screenshots-views-find_screenshot'),
    re_path(r'^remove_from_object/$', views.remove_screenshot_from_object, name='crits-screenshots-views-remove_screenshot_from_object'),
    re_path(r'^render/(?P<_id>\S+)/(?P<thumb>\S+)/$', views.render_screenshot, name='crits-screenshots-views-render_screenshot'),
    re_path(r'^render/(?P<_id>\S+)/$', views.render_screenshot, name='crits-screenshots-views-render_screenshot'),
    re_path(r'^render/$', views.render_screenshot, name='crits-screenshots-views-render_screenshot'),
]
