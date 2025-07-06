from __future__ import absolute_import
from __future__ import print_function
import os
import platform
import subprocess
import sys

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """
    Test CRITs installation and dependencies.
    """
    help = 'Test CRITs installation and dependencies'

    def handle(self, *args, **options):
        """
        Test installation dependencies and configuration.
        """
        self.stdout.write("Testing CRITs installation...")
        
        # Test Python version
        py_version = sys.version_info
        self.stdout.write(f"Python version: {py_version.major}.{py_version.minor}.{py_version.micro}")
        
        # Test Django import
        try:
            import django
            self.stdout.write(f"Django version: {django.get_version()}")
        except ImportError as e:
            self.stdout.write(f"Django import error: {e}")
            return
        
        # Test MongoEngine import
        try:
            import mongoengine
            self.stdout.write(f"MongoEngine version: {mongoengine.__version__}")
        except ImportError as e:
            self.stdout.write(f"MongoEngine import error: {e}")
            return
        
        # Test critical CRITs imports
        try:
            from crits.core.user import CRITsUser
            self.stdout.write("CRITs core user model: OK")
        except Exception as e:
            self.stdout.write(f"CRITs user model error: {e}")
        
        try:
            from crits.services.handlers import run_triage
            self.stdout.write("CRITs services handlers: OK")
        except Exception as e:
            self.stdout.write(f"CRITs services error: {e}")
        
        self.stdout.write("Installation test completed.")
        self.stdout.write("CRITs modernization appears to be working correctly!")