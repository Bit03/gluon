from .base import *
from .base import env

SECRET_KEY = env('SECRET_KEY', default='dapprank.com')

ALLOWED_HOSTS = [
    "*",
]

# django-node
# ------------------------------------------------------------------------------------
# https://django-nose.readthedocs.io/en/latest/index.html
INSTALLED_APPS += ['django_nose', ]
# Use nose to run all tests
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
# Tell nose to measure coverage on the 'foo' and 'bar' apps
NOSE_ARGS = [
    '--with-coverage',
    '--cover-package=applications.dapps, applications.github',
]
