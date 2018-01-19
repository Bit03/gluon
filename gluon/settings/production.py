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