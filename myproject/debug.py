# debug.py
import os
import sys

print("=== DEBUG INFORMATION ===")
print(f"Current directory: {os.getcwd()}")
print(f"Python version: {sys.version}")

print("\n=== FILES IN CURRENT DIRECTORY ===")
for item in os.listdir('.'):
    print(f"  {item}")

print("\n=== CHECKING FOR user_management FOLDER ===")
if os.path.exists('user_management'):
    print("user_management folder exists!")
    print("Contents of user_management folder:")
    for item in os.listdir('user_management'):
        print(f"  {item}")
        
    print("\n=== CHECKING FOR WSGI FILE ===")
    wsgi_path = 'user_management/wsgi.py'
    if os.path.exists(wsgi_path):
        print(f"✓ wsgi.py exists at: {wsgi_path}")
        print("File contents preview:")
        with open(wsgi_path, 'r') as f:
            print(f.read()[:500])  # First 500 chars
    else:
        print(f"✗ wsgi.py NOT found at: {wsgi_path}")
else:
    print("✗ user_management folder NOT found!")

print("\n=== ATTEMPTING TO IMPORT WSGI ===")
try:
    from user_management.wsgi import application
    print("✓ SUCCESS: WSGI module imported!")
except ImportError as e:
    print(f"✗ FAILED: {e}")
    print("\n=== PYTHON PATH ===")
    for path in sys.path:
        print(f"  {path}")