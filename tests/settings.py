from sistersadmin.settings.dev import *

ENV = 'test'

TESTING = True
DEBUG = False

# Disable email sending
EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'

# Disable timezone support for tests. This decreases headaches during comparison.
USE_TZ = False

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s (%(module)s.%(funcName)s): %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        '': {
            'level': 'DEBUG',
            'handlers': [],
        },
        'faker.factory': {
            'level': 'INFO',
        },
        'factory.generate': {
            'level': 'INFO',
        },
    },
}

# Use application/json as default API client request Content-Type
REST_FRAMEWORK['TEST_REQUEST_DEFAULT_FORMAT'] = 'json'
