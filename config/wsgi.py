"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

import environ
from django.core.wsgi import get_wsgi_application

# Initialize environment variables
env = environ.Env()

# Define the base directory (one level up from this file's location)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Load environment variables from the .env file located in BASE_DIR
env_file = os.path.join(BASE_DIR, ".env")
if os.path.exists(env_file):
    environ.Env.read_env(env_file)

# Get the environment setting or default to 'local'
ENVIRONMENT = env("ENVIRONMENT")

# Set the appropriate settings module based on the environment
if ENVIRONMENT == "local":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")
elif ENVIRONMENT == "staging":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.staging")
elif ENVIRONMENT == "production":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.production")
else:
    raise ValueError(f"Unknown ENVIRONMENT: {ENVIRONMENT}")

# Get the WSGI application
application = get_wsgi_application()