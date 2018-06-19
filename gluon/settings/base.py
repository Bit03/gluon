import re

import environ

ROOT_DIR = environ.Path(__file__) - 3  # three folder back (/a/b/c/ - 3 = /)
env = environ.Env()
env.read_env(str(ROOT_DIR.path('.env')))

DEBUG = env('DJANGO_DEBUG', default=False, cast=bool)  # False if not in os.environ

SECRET_KEY = env('SECRET_KEY', default='dapprank.com')

# DATABASES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': env.db('DATABASE_URL', default='sqlite:///db.sqlite3'),
}
DATABASES['default']['ATOMIC_REQUESTS'] = True

# Internationalization
# -------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/1.8/topics/i18n/
TIME_ZONE = 'Asia/Shanghai'

LANGUAGE_CODE = 'zh-hans'

USE_I18N = True

USE_L10N = True

USE_TZ = True

USE_X_FORWARDED_HOST = True

SITE_ID = 1

LOCALE_PATHS = (
    str(ROOT_DIR.path('conf/locale')),
)

ROOT_URLCONF = 'gluon.urls'

WSGI_APPLICATION = 'gluon.wsgi.application'

# APPS
# ------------------------------------------------------------------------------
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
]
REST_FRAMEWORK_APPS = [
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_swagger',
]
THIRD_PARTY_APPS = [
    'django_extensions',
    'django_filters',
    'haystack',
    'taggit',
    'webpack_loader',
]
LOCAL_APPS = [
    'applications.dapps',
    'applications.github',
]
# https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + REST_FRAMEWORK_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# STATIC
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = '/tmp/static'
# https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = '/static/'
# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = [
    str(ROOT_DIR.path('static')),
]
# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

# MIDDLEWARE
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#middleware
MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
]

# TEMPLATES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            str(ROOT_DIR.path('templates'))
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': DEBUG,
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.static',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'string_if_invalid': 'Invalid: "%s"'
        },
    },
]

# Password validation
# --------------------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# django session configure
# -----------------------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/1.11/topics/http/sessions/
SESSION_ENGINE = 'django.contrib.sessions.backends.file'
SESSION_FILE_PATH = '/tmp/'

# REST FRAMEWORK
# ------------------------------------------------------------------------------
# http://www.django-rest-framework.org/api-guide/settings/
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20,
    'DATETIME_FORMAT': '%Y-%m-%d %H:%M:%S',
}

# django haystack
# --------------------------------------------------------------------------
# http://haystacksearch.org/
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': str(ROOT_DIR.path('whoosh_index')),
        'STORAGE': 'file',
        # 'POST_LIMIT': 128 * 1024 * 1024,
        'INCLUDE_SPELLING': True,
        'BATCH_SIZE': 100,
    },
}
HAYSTACK_SEARCH_RESULTS_PER_PAGE = 20

# django-taggit
# --------------------------------------------------------------------------------
# https://django-taggit.readthedocs.io/en/latest/
TAGGIT_CASE_INSENSITIVE = True

# logging
# ---------------------------------------------------------------------------------
#
from .gluon_logging import LOGGING as logging_config

LOGGING = logging_config

# django rest framework jwt
# -----------------------------------------------------------------------------------
#
from gluon.settings.jwt import JWT_AUTH as jwt_auth_config

JWT_AUTH = jwt_auth_config



# disallowed-user-agents
# -----------------------------------------------------------------
# https://docs.djangoproject.com/en/1.11/ref/settings/#disallowed-user-agents
DISALLOWED_USER_AGENTS = [
    re.compile(r'scrapy', re.IGNORECASE),
    re.compile(r'go-http-client', re.IGNORECASE),
    re.compile(r'mj12bot', re.IGNORECASE),
    re.compile(r'yandexbot', re.IGNORECASE),
    re.compile(r'ahrefsbot', re.IGNORECASE),
]
