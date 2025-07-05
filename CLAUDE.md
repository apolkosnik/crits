# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

CRITs (Collaborative Research Into Threats) is a Django-based web application for cyber threat intelligence analysis. It provides a platform for storing, analyzing, and correlating malware samples, indicators, campaigns, and other threat data. The application uses MongoDB as its database and includes a plugin-based service architecture for extensibility.

## Development Commands

### Initial Setup
```bash
# Install Python dependencies (requires Python 3.10+)
pip3 install -r requirements.txt

# First-time setup (installs dependencies, configures database, creates admin user)
sh script/bootstrap

# Start development server (after initial setup)
python3 manage.py runserver 0.0.0.0:8080

# Docker alternative (recommended)
docker build -t crits-modernized .
docker run -d -p 8080:8080 --name crits-app crits-modernized
```

### Core Management Commands
```bash
# Create default database collections
python3 manage.py create_default_collections

# Create database indexes
python3 manage.py create_indexes

# Create roles and permissions
python3 manage.py create_roles

# Test installation and dependencies
python3 manage.py test_install

# User management
python3 manage.py users -a -R UberAdmin -e "email@example.com" -f "First" -l "Last" -o "Org" -u "username"

# Configuration management
python3 manage.py setconfig <setting_name> <value>
```

### Testing
```bash
# Quick modernization verification
python3 verify_modernization.py

# Comprehensive test suite (requires dependencies)
python3 run_tests.py

# Docker-based testing (recommended)
docker-compose -f docker-compose.test.yml build
docker-compose -f docker-compose.test.yml up

# Run Django tests
python3 manage.py test

# Run specific test categories
pytest tests/test_modernization.py -v      # Core modernization tests
pytest tests/test_api_integration.py -v   # API integration tests
pytest tests/test_web_functional.py -v    # Web interface tests

# Run with coverage
pytest --cov=crits --cov-report=html --cov-report=term

# Run specific app tests
python3 manage.py test crits.domains
python3 manage.py test crits.samples
```

### Database Operations
```bash
# MongoDB should be running on localhost:27017
# Start MongoDB (if not running)
sudo sh contrib/mongo/mongod_start.sh

# Database migration and upgrade commands
python3 manage.py upgrade
```

### Fabric Commands (for Vagrant/deployment)
```bash
# Create admin user via Fabric
fab vagrant create_admin_user

# Development setup
fab vagrant dev_setup

# Run server via Fabric
fab vagrant runserver

# Initialize services
fab vagrant init_services
```

## Architecture

### Core Components

**Django Apps Structure:**
- `crits.core`: Base functionality, user management, authentication, and shared utilities
- `crits.actors`: Threat actor tracking and management
- `crits.campaigns`: Campaign correlation and analysis
- `crits.samples`: Malware sample storage and analysis
- `crits.indicators`: IOC management and correlation
- `crits.domains`: Domain and DNS analysis
- `crits.ips`: IP address tracking and geolocation
- `crits.emails`: Email analysis and metadata extraction
- `crits.events`: Event tracking and timeline analysis
- `crits.pcaps`: Network packet capture analysis
- `crits.raw_data`: Unstructured data storage
- `crits.services`: Plugin architecture for analysis services
- `crits.relationships`: Cross-reference relationships between objects

**Database Schema:**
- MongoDB collections are defined in `crits.settings.py` with `COL_*` constants
- Each app typically has a main model class corresponding to its collection
- Uses MongoEngine ODM for database operations
- Supports both old (<0.10) and new (>=0.10) MongoEngine versions

**Service Architecture:**
- Services are plugins that extend core functionality
- Service directories configured via `SERVICE_DIRS` setting
- Each service can provide templates, context processors, and API endpoints
- Services can be run in 'thread' or 'process' mode

### Key Patterns

**URL Structure:**
- Each app has its own `urls.py` with RESTful patterns
- API endpoints available when `ENABLE_API` is True
- All URLs routed through main `crits.urls.py`

**Template Organization:**
- Templates organized by app in `<app>/templates/`
- Shared templates in `crits.core.templates/`
- Service templates auto-discovered from service directories

**Configuration Management:**
- Main config in `crits.settings.py`
- Database config in `crits.config.database.py` (created from example)
- Override settings in `crits.config.overrides.py`
- Runtime config stored in MongoDB `config` collection

**Authentication:**
- Custom authentication backend in `crits.core.user`
- Supports LDAP, remote user, and local authentication
- Role-based permissions with `UberAdmin` super-user role

**File Storage:**
- Supports GridFS (MongoDB) and S3 backends
- Configured via `FILE_DB` setting
- Separate buckets for different file types (samples, pcaps, objects)

## Development Notes

### Modernized Requirements
- **Python 3.10+** and **Django 4.2+ LTS** (modernized from Python 2.7/Django 1.x)
- **MongoEngine 0.27+** (updated from 0.8)
- **MongoDB 6.0+** running on localhost:27017 (updated from 2.6+)
- Development server runs on port 8080 by default
- Debug toolbar available when `ENABLE_DT` is True
- Docker support available for containerized deployment
- Uses Fabric for deployment automation (legacy, consider Docker instead)
- Vagrant configuration available for development environments

### Modernization Changes
- All URL patterns updated from `url()` to `path()/re_path()`
- Import statements modernized: `django.core.urlresolvers` → `django.urls`
- Middleware configuration updated for Django 4.2+
- Template system modernized
- Python 3 compatibility fixes applied throughout codebase
- Docker containerization added for easy deployment

### Docker Quick Start
```bash
# Build and run with Docker Compose (recommended)
docker-compose up -d

# Create initial admin user
docker-compose exec crits python3 manage.py users -R UberAdmin \
  -u admin -p "YourSecurePassword123!" \
  -e "admin@yourorg.com" -f "Admin" -l "User" -o "Your Organization"

# Access CRITs at http://localhost:8080

# Alternative: Build and run manually
docker build -t crits-modernized .
docker run -d -p 8080:8080 --name crits-app crits-modernized
```

### Testing Infrastructure

CRITs includes a comprehensive test suite for the Django 4.2+ and MongoEngine 0.27+ modernization:

**Test Files:**
- `tests/test_modernization.py` - Core modernization compatibility tests
- `tests/test_api_integration.py` - API endpoint and integration testing
- `tests/test_web_functional.py` - Web interface functional testing
- `test_settings.py` - Django test configuration
- `pytest.ini` - Pytest configuration and markers

**Test Categories:**
- **Unit Tests**: Core functionality and model validation
- **Integration Tests**: API endpoints and database operations
- **Functional Tests**: Web interface and form processing
- **Security Tests**: CSRF protection and authentication
- **Performance Tests**: Basic load and query performance

**Running Tests:**
See [TESTING.md](TESTING.md) for comprehensive testing guide.