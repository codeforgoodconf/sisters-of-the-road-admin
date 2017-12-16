"""
This file is meant to simulate production settings.
Don't actually use this file in production
"""

from sistersadmin.settings.base import *

DEBUG = False

SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'barter',
        'USER': 'sisters',
        'PASSWORD': 'sisters',
        'HOST': 'localhost',
        'PORT': '',
    }}

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1'
]
