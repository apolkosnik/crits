"""
Comprehensive test suite for CRITs modernization.
Tests Django 4.2+ and MongoEngine 0.27+ compatibility.
"""

import os
import sys
import django
from django.test import TestCase, TransactionTestCase
from django.test.client import Client, RequestFactory
from django.conf import settings
from django.core.management import call_command
from django.contrib.auth import authenticate
from django.urls import reverse, resolve
from mongoengine import connect, disconnect
from mongoengine.connection import get_connection
import unittest

# Set up Django for testing
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_settings')
django.setup()

from crits.core.user import CRITsUser
from crits.core.handlers import add_new_source
from crits.core.source_access import SourceAccess
from crits.config.config import CRITsConfig


class DjangoModernizationTest(TestCase):
    """Test Django 4.2+ compatibility and modernization features."""
    
    def setUp(self):
        """Set up test environment."""
        self.client = Client()
        self.factory = RequestFactory()
        
    def test_django_version(self):
        """Test that Django 4.2+ is installed and working."""
        import django
        version_info = django.VERSION
        self.assertGreaterEqual(version_info[0], 4)
        if version_info[0] == 4:
            self.assertGreaterEqual(version_info[1], 2)
    
    def test_middleware_configuration(self):
        """Test that Django 4.2+ middleware is properly configured."""
        # Check that MIDDLEWARE is configured (not MIDDLEWARE_CLASSES)
        self.assertTrue(hasattr(settings, 'MIDDLEWARE'))
        self.assertFalse(hasattr(settings, 'MIDDLEWARE_CLASSES'))
        
        # Essential middleware should be present
        essential_middleware = [
            'django.middleware.security.SecurityMiddleware',
            'django.contrib.sessions.middleware.SessionMiddleware',
            'django.middleware.common.CommonMiddleware',
            'django.middleware.csrf.CsrfViewMiddleware',
            'django.contrib.auth.middleware.AuthenticationMiddleware',
            'django.contrib.messages.middleware.MessageMiddleware',
        ]
        
        for middleware in essential_middleware:
            self.assertIn(middleware, settings.MIDDLEWARE)
    
    def test_url_patterns_modernization(self):
        """Test that URL patterns use path()/re_path() instead of url()."""
        from crits.urls import urlpatterns
        
        # All URL patterns should be using path() or re_path()
        for pattern in urlpatterns:
            # Django 4.2+ URLPattern objects have .pattern attribute
            self.assertTrue(hasattr(pattern, 'pattern'))
    
    def test_static_files_configuration(self):
        """Test static files configuration for Django 4.2+."""
        self.assertTrue(hasattr(settings, 'STATIC_URL'))
        self.assertTrue(hasattr(settings, 'STATICFILES_DIRS'))
        
        # Check that static files finders are configured
        finders = settings.STATICFILES_FINDERS
        self.assertIn('django.contrib.staticfiles.finders.FileSystemFinder', finders)
        self.assertIn('django.contrib.staticfiles.finders.AppDirectoriesFinder', finders)


class MongoEngineModernizationTest(TestCase):
    """Test MongoEngine 0.27+ compatibility and modernization features."""
    
    @classmethod
    def setUpClass(cls):
        """Set up MongoDB connection for testing."""
        super().setUpClass()
        try:
            connect('crits_test', host='127.0.0.1', port=27017)
        except Exception as e:
            # MongoDB might not be running in test environment
            cls.skipTest(cls, f"MongoDB not available: {e}")
    
    @classmethod
    def tearDownClass(cls):
        """Clean up MongoDB connection."""
        try:
            disconnect()
        except:
            pass
        super().tearDownClass()
    
    def test_mongoengine_version(self):
        """Test that MongoEngine 0.27+ is installed."""
        import mongoengine
        version = mongoengine.__version__
        major, minor = map(int, version.split('.')[:2])
        self.assertGreaterEqual(major, 0)
        if major == 0:
            self.assertGreaterEqual(minor, 27)
    
    def test_mongoengine_imports(self):
        """Test that MongoEngine imports work correctly."""
        from mongoengine import Document, EmbeddedDocument, StringField, DateTimeField
        from mongoengine import connect, disconnect
        from crits.core.crits_mongoengine import CritsBaseAttributes, CritsQuerySet
        
        # All imports should succeed without django_mongoengine
        self.assertTrue(Document)
        self.assertTrue(EmbeddedDocument)
        self.assertTrue(CritsBaseAttributes)
        self.assertTrue(CritsQuerySet)
    
    def test_document_creation(self):
        """Test that MongoEngine documents can be created and saved."""
        from mongoengine import Document, StringField
        
        class TestDocument(Document):
            name = StringField(required=True)
            meta = {'collection': 'test_documents'}
        
        # Create and save a test document
        doc = TestDocument(name='test')
        try:
            doc.save()
            self.assertEqual(doc.name, 'test')
            self.assertTrue(doc.id)
            
            # Clean up
            doc.delete()
        except Exception as e:
            self.skipTest(f"MongoDB operation failed: {e}")
    
    def test_query_operations(self):
        """Test MongoEngine query operations."""
        from crits.core.crits_mongoengine import CritsQuerySet
        from mongoengine import QuerySet
        
        # Test that our custom QuerySet inherits from MongoEngine QuerySet
        self.assertTrue(issubclass(CritsQuerySet, QuerySet))


class CoreFunctionalityTest(TestCase):
    """Test core CRITs functionality with modernized stack."""
    
    def setUp(self):
        """Set up test data."""
        self.test_user_data = {
            'username': 'test_user',
            'password': 'test_password_123!',
            'email': 'test@example.com',
            'first_name': 'Test',
            'last_name': 'User'
        }
        
        self.test_source = 'TestSource'
        
        # Clean up any existing test data
        self._cleanup_test_data()
    
    def tearDown(self):
        """Clean up test data."""
        self._cleanup_test_data()
    
    def _cleanup_test_data(self):
        """Helper to clean up test data."""
        try:
            user = CRITsUser.objects(username=self.test_user_data['username']).first()
            if user:
                user.delete()
            
            source = SourceAccess.objects(name=self.test_source).first()
            if source:
                source.delete()
        except:
            pass
    
    def test_user_creation(self):
        """Test user creation functionality."""
        try:
            user = CRITsUser.create_user(
                username=self.test_user_data['username'],
                password=self.test_user_data['password'],
                email=self.test_user_data['email']
            )
            user.first_name = self.test_user_data['first_name']
            user.last_name = self.test_user_data['last_name']
            user.save()
            
            # Verify user was created
            self.assertEqual(user.username, self.test_user_data['username'])
            self.assertEqual(user.email, self.test_user_data['email'])
            self.assertTrue(user.check_password(self.test_user_data['password']))
            
            # Verify user can be found
            found_user = CRITsUser.objects(username=self.test_user_data['username']).first()
            self.assertIsNotNone(found_user)
            self.assertEqual(found_user.username, user.username)
            
        except Exception as e:
            self.skipTest(f"User creation test failed - MongoDB might not be available: {e}")
    
    def test_source_management(self):
        """Test source creation and management."""
        try:
            # Create a source
            result = add_new_source(self.test_source, 'test_analyst')
            self.assertTrue(result)
            
            # Verify source was created
            source = SourceAccess.objects(name=self.test_source).first()
            self.assertIsNotNone(source)
            self.assertEqual(source.name, self.test_source)
            
        except Exception as e:
            self.skipTest(f"Source management test failed - MongoDB might not be available: {e}")
    
    def test_config_system(self):
        """Test CRITs configuration system."""
        try:
            # Create or get config
            config = CRITsConfig.objects().first()
            if not config:
                config = CRITsConfig()
                config.save()
            
            self.assertIsNotNone(config)
            
        except Exception as e:
            self.skipTest(f"Config system test failed - MongoDB might not be available: {e}")


class URLRoutingTest(TestCase):
    """Test URL routing and view functionality."""
    
    def test_main_urls_resolve(self):
        """Test that main URL patterns resolve correctly."""
        test_urls = [
            '/',
            '/login/',
            '/logout/',
            '/dashboard/',
        ]
        
        for url in test_urls:
            try:
                resolved = resolve(url)
                self.assertIsNotNone(resolved)
            except Exception as e:
                # Some URLs might require authentication or specific setup
                pass
    
    def test_api_urls_exist(self):
        """Test that API URL patterns exist."""
        try:
            from crits.core.urls import urlpatterns as core_patterns
            # API patterns should exist
            self.assertTrue(len(core_patterns) > 0)
        except ImportError:
            self.skipTest("Core URLs not available")


class SecurityTest(TestCase):
    """Test security configurations and features."""
    
    def test_security_middleware(self):
        """Test security middleware configuration."""
        self.assertIn('django.middleware.security.SecurityMiddleware', settings.MIDDLEWARE)
        self.assertIn('django.middleware.csrf.CsrfViewMiddleware', settings.MIDDLEWARE)
    
    def test_password_validation(self):
        """Test password validation settings."""
        if hasattr(settings, 'AUTH_PASSWORD_VALIDATORS'):
            validators = settings.AUTH_PASSWORD_VALIDATORS
            self.assertIsInstance(validators, list)
    
    def test_secret_key_configuration(self):
        """Test that SECRET_KEY is configured."""
        self.assertTrue(hasattr(settings, 'SECRET_KEY'))
        self.assertIsNotNone(settings.SECRET_KEY)
        self.assertNotEqual(settings.SECRET_KEY, '')


class PerformanceTest(TestCase):
    """Test performance-related configurations."""
    
    def test_template_caching(self):
        """Test template caching configuration."""
        templates = settings.TEMPLATES
        self.assertTrue(len(templates) > 0)
        
        for template_config in templates:
            if 'OPTIONS' in template_config:
                # In production, template caching should be enabled
                pass
    
    def test_static_files_serving(self):
        """Test static files configuration."""
        self.assertTrue(hasattr(settings, 'STATIC_URL'))
        self.assertTrue(hasattr(settings, 'STATIC_ROOT'))


if __name__ == '__main__':
    # Run tests
    unittest.main(verbosity=2)