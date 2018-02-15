from .settings import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'gluon',
        'USER': 'gluon',
        'PASSWORD': 'gluon1@#',
        'HOST': "10.132.11.59",
        'PORT': 3306,
        'OPTIONS': {
            'charset': 'utf8mb4',
            'init_command': "SET storage_engine=INNODB, sql_mode='STRICT_TRANS_TABLES'",
        }
    }
}

ALLOWED_HOSTS = ["*"]

# '''
#     session configure
# '''
# SESSION_ENGINE = 'django.contrib.sessions.backends.file'
# SESSION_FILE_PATH = '/tmp/'

# static
STATIC_ROOT = '/data/www/static/'
STATIC_URL = '//static.dapprank.com/static/'


##
#   rest framework
##
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20,
    'DATETIME_FORMAT': '%Y-%m-%d %H:%M:%S',
}


###
# django compress
###

from .compress import *

# COMPRESS_ROOT