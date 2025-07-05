from __future__ import absolute_import
import ast
import datetime
import json
import logging
import copy

from django.http import HttpResponse
from multiprocessing import Process
from threading import Thread, local
import six


from multiprocessing.pool import Pool, ThreadPool

    __service_process_pool__ = None
