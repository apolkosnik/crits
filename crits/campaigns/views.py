from __future__ import absolute_import
import datetime
import json

from bson import json_util
from django.conf import settings
from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse
        return render(request, "error.html", {"error": error})
