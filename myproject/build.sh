#!/usr/bin/env bash
# build.sh

set -e  # Exit on error

echo "========== STARTING BUILD =========="
echo "Current directory: $(pwd)"
echo "Python version: $(python --version)"
echo "====================================="

# Install dependencies
echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo "========== FILE STRUCTURE =========="
echo "=== Root directory contents ==="
ls -la

echo "=== Checking user_management folder ==="
if [ -d "user_management" ]; then
    echo "✓ user_management directory exists"
    echo "Contents of user_management:"
    ls -la user_management/
    
    if [ -f "user_management/wsgi.py" ]; then
        echo "✓ wsgi.py FOUND"
        echo "First few lines of wsgi.py:"
        head -10 user_management/wsgi.py
    else
        echo "✗ wsgi.py NOT FOUND"
    fi
else
    echo "✗ user_management directory NOT FOUND"
fi

echo "=== Checking for manage.py ==="
if [ -f "manage.py" ]; then
    echo "✓ manage.py exists"
else
    echo "✗ manage.py NOT FOUND"
fi

echo "========== PYTHON DEBUG =========="
python -c "
import os
import sys

print('Current working directory:', os.getcwd())
print('Python path:')
for path in sys.path:
    print('  ', path)

print('\nFiles in current directory:')
for item in os.listdir('.'):
    print('  ', item)

print('\n=== Testing WSGI import ===')
try:
    from user_management.wsgi import application
    print('✓ SUCCESS: WSGI application imported!')
    
    # Test Django setup
    import django
    from django.conf import settings
    print('✓ Django settings loaded')
    print('✓ DEBUG mode:', settings.DEBUG)
    print('✓ Allowed hosts:', settings.ALLOWED_HOSTS)
    
except ImportError as e:
    print('✗ ImportError:', e)
    print('\nTrying to debug the issue:')
    try:
        import user_management
        print('✓ user_management package can be imported')
        print('✓ user_management location:', user_management.__file__)
    except ImportError as e2:
        print('✗ Cannot import user_management at all:', e2)
        
except Exception as e:
    print('✗ Other error:', e)
"

echo "========== COLLECT STATIC =========="
python manage.py collectstatic --noinput

echo "========== BUILD COMPLETE =========="