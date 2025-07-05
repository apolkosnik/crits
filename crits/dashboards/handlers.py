"""
This File will often refer to 'default dashboard tables.' They currently are:
Counts, Top Campaigns, Recent Indicators, Recent Emails, and
Recent Samples in that order. The user has the ability to change they're
positioning, size, columns, and sort order but they are always there and their
names cannot be changed.
"""
from __future__ import absolute_import
from __future__ import print_function
from crits.dashboards.dashboard import SavedSearch, Dashboard
from crits.core.crits_mongoengine import json_handler
from crits.core.user_tools import get_acl_object
from mongoengine import Q
import six
