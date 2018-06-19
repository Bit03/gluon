from .base import *
from .base import env

env.read_env(str(ROOT_DIR.path('.env')))

DEBUG = env('DJANGO_DEBUG', default=False, cast=bool)  # False if not in os.environ
# DEBUG = True

SECRET_KEY = env('SECRET_KEY', default='dapprank.com')

ALLOWED_HOSTS = [
    "*",
]

# django-node
# ------------------------------------------------------------------------------------
# https://django-nose.readthedocs.io/en/latest/index.html
# INSTALLED_APPS += ['django_nose', ]
# Use nose to run all tests
# TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

# Tell nose to measure coverage on the 'foo' and 'bar' apps
# NOSE_ARGS = [
#     '--with-coverage',
#     '--cover-package=dapps,github',
# ]

# django-debug-toolbar
# ------------------------------------------------------------------------------
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#prerequisites
INSTALLED_APPS += ['debug_toolbar']  # noqa F405
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#middleware
MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'views.middleware.dev_cors_middleware',
]
# https://django-debug-toolbar.readthedocs.io/en/latest/configuration.html#debug-toolbar-config
DEBUG_TOOLBAR_CONFIG = {
    'DISABLE_PANELS': [
        'debug_toolbar.panels.redirects.RedirectsPanel',
    ],
    'SHOW_TEMPLATE_CONTEXT': True,
}
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#internal-ips
INTERNAL_IPS = ['127.0.0.1']


SHELL_PLUS = "ptpython"


WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': 'static/',
        'STATS_FILE': str(ROOT_DIR.path('webpack-stats.prod.json')),
    }
}
