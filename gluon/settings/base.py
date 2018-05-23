import environ

ROOT_DIR = environ.Path(__file__) - 3  # three folder back (/a/b/c/ - 3 = /)
env = environ.Env()
env.read_env(str(ROOT_DIR.path('.env')))

DEBUG = env('DJANGO_DEBUG', default=True)  # False if not in os.environ

# DATABASES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': env.db('DATABASE_URL', default=str(ROOT_DIR.path('db.sqlite3'))),
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
]
THIRD_PARTY_APPS = [
    'django_extensions',
    'django_filters',
    'haystack',
    'compressor',
    'taggit',
    'bulma',
]
LOCAL_APPS = [
    'dapps',
    'github',
]