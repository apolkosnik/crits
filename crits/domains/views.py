from __future__ import absolute_import
import six.moves.urllib.request, six.moves.urllib.parse, six.moves.urllib.error
import json

from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import user_passes_test
        return render(request, 'error.html', {'error': 'Expected POST'})
