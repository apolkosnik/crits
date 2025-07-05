"""
Test settings for CRITs modernized version.
Override production settings for testing environment.
"""

from crits.settings import *
import os

# Test database configuration
TESTING = True

# Use separate test database
MONGO_DATABASE = 'crits_test'

# Disable external services during testing
ENABLE_API = False
ENABLE_NOTICATIONS = False

# Speed up password hashing for tests
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.MD5PasswordHasher',
]

# Disable migrations during testing
class DisableMigrations:
    def __contains__(self, item):
        return True
    
    def __getitem__(self, item):
        return None

MIGRATION_MODULES = DisableMigrations()

# Test-specific logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'WARNING',
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'WARNING',
            'propagate': False,
        },
    },
}

# Disable caching during tests
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

# Test media settings
MEDIA_ROOT = '/tmp/crits_test_media'
STATIC_ROOT = '/tmp/crits_test_static'

# Disable query caching for tests
QUERY_CACHING = False

# Security settings for tests
SECRET_KEY = 'test-secret-key-not-for-production'
DEBUG = True
ALLOWED_HOSTS = ['testserver', 'localhost', '127.0.0.1']

# Email backend for testing
EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'