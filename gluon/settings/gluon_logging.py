# logging
# --------------------------------------------------------
# https://docs.djangoproject.com/en/1.11/topics/logging/
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
            # 'format': '[%(asctime)s.%(msecs)d] %(levelname)s [%(module)s:%(funcName)s:%(lineno)d]- %(message)s',
        },
        'error': {
            'format': '[%(asctime)s.%(msecs)d] [%(module)s:%(funcName)s:%(lineno)d]- %(message)s',
        },
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'formatter': 'error',
            'filename': '/tmp/django.log',
            'mode': 'a',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file', 'console'],
            'propagate': True,
            'level': 'INFO',
        },
        'django.request': {
            'handlers': ['file', ],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}