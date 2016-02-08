from base import *

DEBUG = False

TEMPLATE_DEBUG = DEBUG


#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.mysql',
#        'NAME': 'pyHEPI_service',
#        'HOST': '',
#        'USER': '',
#        'PASSWORD': '',
#        'CONN_MAX_AGE': 600,
#    }
#}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR.child('templates'),
            os.path.join(PROJECT_DIR.child('service'), 'templates', 'service'),
        ],
        #'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
            'debug': False,
        },
    },
]


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
        'KEY_PREFIX': 'key_prefix'
    }
}

ALLOWED_HOSTS = ['.{{cookiecutter.domain_name}}', '{{cookiecutter.domain_name}}.'] # subdomains and FQDN

ROOT_URLCONF = '{{cookiecutter.repo_name}}.urls'