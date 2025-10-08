#!/usr/bin/env bash
# build.sh

echo "========== STARTING BUILD =========="
echo "Current directory: $(pwd)"
echo "====================================="

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

echo "========== FILE STRUCTURE =========="
echo "=== Root directory contents ==="
ls -la

echo "=== Recursive Python files ==="
find . -name "*.py" -type f | sort

echo "=== Checking user_management ==="
if [ -d "user_management" ]; then
    echo "user_management directory exists"
    ls -la user_management/
    
    if [ -f "user_management/wsgi.py" ]; then
        echo "✓ wsgi.py FOUND in user_management/"
        echo "=== wsgi.py contents ==="
        head -20 user_management/wsgi.py
    else
        echo "✗ wsgi.py NOT FOUND in user_management/"
    fi
else
    echo "✗ user_management directory NOT FOUND"
fi

echo "========== PYTHON DEBUG =========="
python -c "
import os, sys
print('Python path:')
for p in sys.path:
    print('  ', p)
print('Current dir files:', os.listdir('.'))
try:
    from user_management.wsgi import application
    print('✓ SUCCESS: WSGI imported!')
except Exception as e:
    print('✗ FAILED:', e)
    print('Trying to find module...')
    import importlib.util
    spec = importlib.util.find_spec('user_management.wsgi')
    print('Module spec:', spec)
"

echo "========== BUILD COMPLETE =========="