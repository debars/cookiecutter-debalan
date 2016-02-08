# -*- coding: utf-8 -*-

"""
Django settings for manybooks project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

import os
from unipath import Path
from os.path import realpath

# Normally you should not import ANYTHING from Django directly
# into your settings, but ImproperlyConfigured is an exception.
from django.core.exceptions import ImproperlyConfigured

def get_env_variable(var_name):
    '''Get the environment variable or return exception.'''
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = "Set the {} environment variable".format(var_name)
        raise ImproperlyConfigured(error_msg)

#BASE_DIR = os.path.dirname(os.path.dirname(__file__))
BASE_DIR = Path(__file__).ancestor(2)

#PROJECT_DIR = os.sep.join(os.path.abspath(os.path.dirname(__file__)).split(os.sep)[:-2])
PROJECT_DIR = Path(__file__).ancestor(3)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

ADMINS = (
    ('alan.schmitz88@gmail.com'),
)

MANAGERS = ADMINS

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_env_variable("..._SECRET_KEY")

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'djangocms_admin_style',
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = '{{ cookiecutter.repo_name }}.urls'

WSGI_APPLICATION = '{{ cookiecutter.repo_name }}.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_env_variable("..._DB"),
        'USER': get_env_variable("..._DB_USER"),
        'PASSWORD': get_env_variable("..._DB_PASSWD"),
        'HOST': get_env_variable("..._DB_HOST"),
        'PORT': get_env_variable("..._DB_PORT"),
        'CONN_MAX_AGE': 600,
    },
    'local_sqlite_db': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': realpath('mysqlite.db'),
    },
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

TIME_ZONE = 'America/Denver'

LANGUAGES = [
    ('en', 'English'),
    ('de', 'Deutsch')
]


LANGUAGE_CODE = 'en'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

MEDIA_ROOT = BASE_DIR.child("media")

MEDIA_URL = '/media/'

STATIC_ROOT = BASE_DIR.child("static")

STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASE_DIR.child('static'), 'pyHEPI_service'),
    #BASE_DIR.child("assets"),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# List of callables that know how to import templates from various sources.
#TEMPLATE_LOADERS = (
#    'django.template.loaders.filesystem.Loader',
#    'django.template.loaders.app_directories.Loader',
#)

#TEMPLATE_CONTEXT_PROCESSORS = (
#    'django.contrib.auth.context_processors.auth',
#    'django.core.context_processors.debug',
#    'django.core.context_processors.i18n',
#    'django.core.context_processors.media',
#    'django.core.context_processors.static',
#    'django.core.context_processors.tz',
#    'django.contrib.messages.context_processors.messages',
#    'django.core.context_processors.request',
#)

#TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
#    os.path.join(BASE_DIR, "templates"),
#)

TEST_RUNNER = 'django.test.runner.DiscoverRunner'

LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'filters': {
            'require_debug_false': {
                '()': 'django.utils.log.RequireDebugFalse'
            }
        },
        'handlers': {
            'mail_admins': {
                'level': 'ERROR',
                'filters': ['require_debug_false'],
                'class': 'django.utils.log.AdminEmailHandler'
            }
        },
        'loggers': {
            'django.request': {
                'handlers': ['mail_admins'],
                'level': 'ERROR',
                'propagate': True,
            },
        }
    }

CKEDITOR_UPLOAD_PATH = 'uploads/'

CKEDITOR_JQUERY_URL = 'https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js'

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': None,
    },
}
