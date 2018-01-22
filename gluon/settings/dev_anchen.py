from .dev import *
DEBUG = True

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'gluon',
        'USER': 'root',
        'PASSWORD': 'mypass',
        'HOST': "127.0.0.1",
        'PORT': 3306,
        'OPTIONS': {
            'charset': 'utf8mb4',
        }
    }
}

ALLOWED_HOSTS = ["*"]

'''
    session configure
'''
SESSION_ENGINE = 'django.contrib.sessions.backends.file'
SESSION_FILE_PATH = '/tmp/'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, '../templates'), ],
        # 'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# static
STATIC_ROOT = '/data/www/static/'
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, '../static'),]
