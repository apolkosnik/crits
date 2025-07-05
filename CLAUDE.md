# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

CRITs (Collaborative Research Into Threats) is a Django-based web application for cyber threat intelligence analysis. It provides a platform for storing, analyzing, and correlating malware samples, indicators, campaigns, and other threat data. The application uses MongoDB as its database and includes a plugin-based service architecture for extensibility.

## Development Commands

### Initial Setup
```bash
# First-time setup (installs dependencies, configures database, creates admin user)
sh script/bootstrap

# Start development server (after initial setup)
sh script/server

# Alternative development server start
python manage.py runserver 0.0.0.0:8080
```

### Core Management Commands
```bash
# Create default database collections
python manage.py create_default_collections

# Create database indexes
python manage.py create_indexes

# Create roles and permissions
python manage.py create_roles

# Test installation and dependencies
python manage.py test_install

# User management
python manage.py users -a -R UberAdmin -e "email@example.com" -f "First" -l "Last" -o "Org" -u "username"

# Configuration management
python manage.py setconfig <setting_name> <value>
```

### Testing
```bash
# Run Django tests
python manage.py test

# Run specific app tests
python manage.py test crits.domains
python manage.py test crits.samples
```

### Database Operations
```bash
# MongoDB should be running on localhost:27017
# Start MongoDB (if not running)
sudo sh contrib/mongo/mongod_start.sh

# Database migration and upgrade commands
python manage.py upgrade
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

- Uses Python 2.7 and Django < 2.0
- Requires MongoDB 2.6+ running on localhost:27017
- Development server runs on port 8080 by default
- Debug toolbar available when `ENABLE_DT` is True
- Uses Fabric for deployment automation
- Vagrant configuration available for development environments