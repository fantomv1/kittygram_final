import os
from pathlib import Path

from django.core.management.utils import get_random_secret_key
from dotenv import load_dotenv

load_dotenv()


def get_secret_key():
    if os.getenv("SETTINGS_SECRET_KEY") is not None:
        return os.getenv("SETTINGS_SECRET_KEY")
    return get_random_secret_key()


def get_debug_bool():
    if os.getenv("SETTINGS_DEBUG") is not None:
        return os.getenv("SETTINGS_DEBUG").lower() == "true"
    return True


def get_allowed_host():
    if os.getenv("SETTINGS_ALLOWED_HOSTS") is not None:
        return os.getenv("SETTINGS_ALLOWED_HOSTS").split()
    return []


DATABASES_POSTGRESQL = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB', 'django'),
        'USER': os.getenv('POSTGRES_USER', 'django'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', ''),
        'HOST': os.getenv('DB_HOST', ''),
        'PORT': os.getenv('DB_PORT', 5432)
    }
}

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASES_SQLITE = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


def get_databases():
    if (os.getenv("SETTINGS_DATABASES_SQLITE") is not None
       and os.getenv("SETTINGS_DATABASES_SQLITE").lower() == "true"):
        return DATABASES_SQLITE
    return DATABASES_POSTGRESQL
