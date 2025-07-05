#!/usr/bin/env python3
"""
Comprehensive test runner for CRITs modernization.
Runs all test suites and generates reports.
"""

import os
import sys
import subprocess
import time
import json
from pathlib import Path

# Add current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Set Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_settings')

# Import Django and configure
import django
django.setup()


def run_command(cmd, description):
    """Run a command and return the result."""
    print(f"\n{'='*60}")
    print(f"Running: {description}")
    print(f"Command: {cmd}")
    print(f"{'='*60}")
    
    start_time = time.time()
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=300)
        end_time = time.time()
        
        print(f"Duration: {end_time - start_time:.2f} seconds")
        print(f"Return code: {result.returncode}")
        
        if result.stdout:
            print("STDOUT:")
            print(result.stdout)
        
        if result.stderr:
            print("STDERR:")
            print(result.stderr)
        
        return result.returncode == 0, result.stdout, result.stderr
    
    except subprocess.TimeoutExpired:
        print("Command timed out!")
        return False, "", "Command timed out"
    except Exception as e:
        print(f"Error running command: {e}")
        return False, "", str(e)


def check_dependencies():
    """Check that required dependencies are available."""
    print("Checking dependencies...")
    
    checks = [
        ("python3 -c 'import django; print(f\"Django {django.get_version()}\")'", "Django"),
        ("python3 -c 'import mongoengine; print(f\"MongoEngine {mongoengine.__version__}\")'", "MongoEngine"),
        ("python3 -c 'import pytest; print(f\"pytest {pytest.__version__}\")'", "pytest"),
    ]
    
    all_good = True
    for cmd, name in checks:
        success, stdout, stderr = run_command(cmd, f"Check {name}")
        if not success:
            print(f"❌ {name} check failed")
            all_good = False
        else:
            print(f"✅ {name} available: {stdout.strip()}")
    
    return all_good


def run_django_checks():
    """Run Django system checks."""
    print("\n" + "="*60)
    print("Running Django System Checks")
    print("="*60)
    
    success, stdout, stderr = run_command("python3 manage.py check", "Django system check")
    
    if success:
        print("✅ Django system checks passed")
        return True
    else:
        print("❌ Django system checks failed")
        return False


def run_unit_tests():
    """Run unit tests."""
    print("\n" + "="*60)
    print("Running Unit Tests")
    print("="*60)
    
    # Run existing CRITs tests
    success1, stdout1, stderr1 = run_command(
        "python3 manage.py test crits.core.tests crits.domains.tests crits.emails.tests --verbosity=2",
        "Existing CRITs unit tests"
    )
    
    # Run new modernization tests
    success2, stdout2, stderr2 = run_command(
        "python3 -m pytest tests/test_modernization.py -v",
        "Modernization unit tests"
    )
    
    if success1 and success2:
        print("✅ All unit tests passed")
        return True
    else:
        print("❌ Some unit tests failed")
        return False


def run_integration_tests():
    """Run integration tests."""
    print("\n" + "="*60)
    print("Running Integration Tests")
    print("="*60)
    
    success, stdout, stderr = run_command(
        "python3 -m pytest tests/test_api_integration.py -v",
        "API integration tests"
    )
    
    if success:
        print("✅ Integration tests passed")
        return True
    else:
        print("❌ Integration tests failed")
        return False


def run_functional_tests():
    """Run functional tests."""
    print("\n" + "="*60)
    print("Running Functional Tests")
    print("="*60)
    
    success, stdout, stderr = run_command(
        "python3 -m pytest tests/test_web_functional.py -v",
        "Web functional tests"
    )
    
    if success:
        print("✅ Functional tests passed")
        return True
    else:
        print("❌ Functional tests failed")
        return False


def run_security_tests():
    """Run security-focused tests."""
    print("\n" + "="*60)
    print("Running Security Tests")
    print("="*60)
    
    # Django security check
    success1, stdout1, stderr1 = run_command(
        "python3 manage.py check --deploy",
        "Django security check"
    )
    
    # Custom security tests (if any)
    success2 = True  # Placeholder for additional security tests
    
    if success1 and success2:
        print("✅ Security tests passed")
        return True
    else:
        print("❌ Security tests failed")
        return False


def run_performance_tests():
    """Run basic performance tests."""
    print("\n" + "="*60)
    print("Running Performance Tests")
    print("="*60)
    
    # Basic import time test
    start_time = time.time()
    success, stdout, stderr = run_command(
        "python3 -c 'import crits.settings; print(\"Settings imported successfully\")'",
        "Import performance test"
    )
    end_time = time.time()
    
    import_time = end_time - start_time
    print(f"Settings import time: {import_time:.3f} seconds")
    
    if success and import_time < 5.0:
        print("✅ Performance tests passed")
        return True
    else:
        print("❌ Performance tests failed")
        return False


def generate_test_report(results):
    """Generate a test report."""
    print("\n" + "="*80)
    print("TEST SUMMARY REPORT")
    print("="*80)
    
    total_tests = len(results)
    passed_tests = sum(1 for result in results.values() if result)
    failed_tests = total_tests - passed_tests
    
    print(f"Total test suites: {total_tests}")
    print(f"Passed: {passed_tests}")
    print(f"Failed: {failed_tests}")
    print(f"Success rate: {(passed_tests/total_tests)*100:.1f}%")
    
    print("\nDetailed Results:")
    for test_name, result in results.items():
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"  {test_name:<30} {status}")
    
    # Overall result
    if failed_tests == 0:
        print("\n🎉 ALL TESTS PASSED! CRITs modernization is successful.")
        return True
    else:
        print(f"\n⚠️  {failed_tests} test suite(s) failed. Review output above.")
        return False


def main():
    """Main test runner."""
    print("CRITs Modernization Test Suite")
    print("="*80)
    print("Testing Django 4.2+ and MongoEngine 0.27+ compatibility")
    print("="*80)
    
    # Check dependencies first
    if not check_dependencies():
        print("\n❌ Dependency checks failed. Please install required packages.")
        return 1
    
    # Run all test suites
    test_results = {}
    
    test_suites = [
        ("Django System Checks", run_django_checks),
        ("Unit Tests", run_unit_tests),
        ("Integration Tests", run_integration_tests),
        ("Functional Tests", run_functional_tests),
        ("Security Tests", run_security_tests),
        ("Performance Tests", run_performance_tests),
    ]
    
    for test_name, test_func in test_suites:
        try:
            result = test_func()
            test_results[test_name] = result
        except Exception as e:
            print(f"\n❌ Error running {test_name}: {e}")
            test_results[test_name] = False
    
    # Generate final report
    success = generate_test_report(test_results)
    
    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())