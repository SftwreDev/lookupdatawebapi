#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

import environ

# Set the base directory to the directory containing manage.py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

env = environ.Env()
# Take environment variables from .env file
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))

ENVIRONMENT = env(
    "ENVIRONMENT"
)  # Default to 'local' if ENVIRONMENT is not set


def main():
    """Run administrative tasks."""
    if ENVIRONMENT == "local":
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")
    elif ENVIRONMENT == "staging":
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.staging")
    elif ENVIRONMENT == "production":
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.production")
    else:
        raise ValueError(f"Unknown ENVIRONMENT: {ENVIRONMENT}")

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
