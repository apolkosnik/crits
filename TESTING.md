# CRITs Modernization Testing Guide

This document describes the comprehensive test suite created for the CRITs modernization to Django 4.2+ and MongoEngine 0.27+.

## Overview

The test suite ensures that all modernization changes work correctly and maintain compatibility with existing CRITs functionality while utilizing the latest framework versions.

## Test Structure

### 1. Core Test Files

#### `test_settings.py`
Django test configuration optimized for testing:
- Separate test database (`crits_test`)
- Disabled external services during testing
- Fast password hashing for tests
- Proper logging configuration

#### `pytest.ini`
Pytest configuration with:
- Django test integration
- Test markers for categorization
- Coverage reporting setup
- Warning filters

### 2. Test Suites

#### `tests/test_modernization.py`
**Core Modernization Compatibility Tests**
- Django 4.2+ version verification
- Middleware configuration validation
- URL pattern modernization checks
- MongoEngine 0.27+ import testing
- Document creation and query operations
- Security configuration validation

#### `tests/test_api_integration.py`
**API Integration Tests**
- Authentication endpoint testing
- Authorization requirement validation
- JSON API response format verification
- CRUD operations testing
- CSRF protection validation
- Input validation and security testing
- Performance and bulk operations

#### `tests/test_web_functional.py`
**Web Interface Functional Tests**
- Template rendering verification
- Static file serving validation
- Form functionality testing
- Responsiveness and accessibility checks
- JavaScript/AJAX endpoint testing
- Browser compatibility features

### 3. Test Runners

#### `run_tests.py`
Comprehensive test runner that executes:
1. **Dependency Checks** - Verify required packages
2. **Django System Checks** - Framework validation
3. **Unit Tests** - Core functionality testing
4. **Integration Tests** - API endpoint testing
5. **Functional Tests** - Web interface testing
6. **Security Tests** - Security configuration validation
7. **Performance Tests** - Basic performance checks

Features:
- Detailed progress reporting
- Error capture and display
- Comprehensive final report
- Timeout protection

#### `verify_modernization.py`
Quick verification script that checks:
- File existence and structure
- Requirements content validation
- URL pattern modernization
- Docker configuration
- Test setup completion

## Docker Testing Environment

### `Dockerfile.test`
Test-specific Docker image including:
- Ubuntu 22.04 base
- Python 3.10+ runtime
- All CRITs dependencies
- Testing frameworks (pytest, coverage)
- Development tools

### `docker-compose.test.yml`
Isolated test environment with:
- MongoDB test database
- CRITs test application
- Persistent test data volumes
- Separate network isolation

## Running Tests

### Local Testing (Quick Verification)
```bash
# Quick modernization verification
python3 verify_modernization.py

# Basic functionality check (requires dependencies)
python3 run_tests.py
```

### Docker Testing (Full Suite)
```bash
# Build test environment
docker-compose -f docker-compose.test.yml build

# Run complete test suite
docker-compose -f docker-compose.test.yml up

# Run specific test categories
docker-compose -f docker-compose.test.yml run crits-test pytest tests/test_modernization.py -v
```

### Production Verification
```bash
# Start production environment
docker-compose up -d

# Verify services are working
docker-compose exec crits python3 verify_modernization.py

# Check application health
curl http://localhost:8080/
```

## Test Categories

### Unit Tests
- Model creation and validation
- Core functionality verification
- Framework compatibility testing

### Integration Tests
- API endpoint functionality
- Database operations
- Authentication and authorization

### Functional Tests
- Web interface operation
- Form processing
- Static file serving

### Security Tests
- CSRF protection
- Input validation
- Authentication requirements

### Performance Tests
- Basic load testing
- Query performance
- Import/export operations

## Test Markers

Tests are categorized with pytest markers:

```bash
# Run only unit tests
pytest -m unit

# Run only integration tests
pytest -m integration

# Run only functional tests
pytest -m functional

# Skip slow tests
pytest -m "not slow"
```

## Coverage Reporting

Generate test coverage reports:

```bash
# Run tests with coverage
pytest --cov=crits --cov-report=html --cov-report=term

# View HTML coverage report
open htmlcov/index.html
```

## Continuous Integration

The test suite is designed for CI/CD integration:

```yaml
# Example GitHub Actions workflow
name: CRITs Tests
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Build and test
      run: |
        docker-compose -f docker-compose.test.yml build
        docker-compose -f docker-compose.test.yml up --exit-code-from crits-test
```

## Test Data Management

- Test database automatically created/destroyed
- Isolated test collections
- Cleanup after each test run
- No impact on production data

## Troubleshooting

### Common Issues

1. **MongoDB Connection Failed**
   ```bash
   # Check MongoDB is running
   docker-compose ps mongodb
   
   # Restart MongoDB service
   docker-compose restart mongodb
   ```

2. **Import Errors**
   ```bash
   # Verify Python path
   echo $PYTHONPATH
   
   # Install dependencies
   pip3 install -r requirements.txt
   ```

3. **Permission Errors**
   ```bash
   # Fix file permissions
   sudo chown -R $USER:$USER .
   chmod +x run_tests.py verify_modernization.py
   ```

### Test Debugging

Enable verbose output:
```bash
# Verbose pytest output
pytest -v -s

# Debug test runner
python3 run_tests.py --debug

# Django test debugging
python3 manage.py test --debug-mode
```

## Extending Tests

### Adding New Tests

1. Create test file in `tests/` directory
2. Follow naming convention: `test_*.py`
3. Use appropriate test markers
4. Include in test runner if needed

### Custom Test Configuration

Modify `test_settings.py` for specific test requirements:
- Database configuration
- Service mocking
- Environment variables

## Validation Results

The comprehensive test suite validates:

✅ **Framework Compatibility**
- Django 4.2+ features and deprecations
- MongoEngine 0.27+ functionality
- Python 3.10+ compatibility

✅ **Modernization Success**
- URL pattern updates (url() → path()/re_path())
- Middleware configuration (MIDDLEWARE vs MIDDLEWARE_CLASSES)
- Template and static file handling

✅ **Security Compliance**
- CSRF protection enabled
- Security middleware configured
- Input validation implemented

✅ **Performance Optimization**
- Query optimization
- Caching configuration
- Static file optimization

✅ **Deployment Readiness**
- Docker containerization
- Production configuration
- Database migrations

## Support

For test-related issues:
1. Check test output for specific error messages
2. Review Docker logs: `docker-compose logs`
3. Verify dependencies: `python3 verify_modernization.py`
4. Consult deployment documentation: `DEPLOYMENT.md`

The test suite ensures CRITs modernization is complete, functional, and ready for production deployment.