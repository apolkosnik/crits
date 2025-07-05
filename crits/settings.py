# CRITs environment chooser

from __future__ import absolute_import
from __future__ import print_function
import errno
import glob
import os
import sys
import django
import subprocess

from pymongo import ReadPreference
from mongoengine import connect
from mongoengine import __version__ as mongoengine_version

from distutils.version import StrictVersion

sys.path.insert(0, os.path.dirname(__file__))

# calculated paths for django and the site
# used as starting points for various other paths
DJANGO_ROOT = os.path.dirname(os.path.realpath(django.__file__))
SITE_ROOT = os.path.dirname(os.path.realpath(__file__))

WSGI_APPLICATION = 'wsgi.application'

TEST_RUNNER = 'django.test.runner.DiscoverRunner'
# Version
CRITS_VERSION = '4-master'

#the following gets the current git hash to be displayed in the footer and
#hides it if it is not a git repo
    exec(compile(open(csfile, "rb").read(), csfile, 'exec'))
