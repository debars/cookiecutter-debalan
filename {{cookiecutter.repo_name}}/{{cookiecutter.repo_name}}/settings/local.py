# -*- coding: utf-8 -*-
from base import *


DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '{{cookiecutter.project_name}}',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': '',
        'CONN_MAX_AGE': 600,
    }
}

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}

MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)

TEMPLATE_CONTEXT_PROCESSORS += ('django.core.context_processors.debug',)

INTERNAL_IPS = ('127.0.0.1',)

INSTALLED_APPS += (
    'debug_toolbar',
)


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

SECRET_KEY = '#'