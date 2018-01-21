from sistersadmin.settings.base import *

import dj_database_url

db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)

SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")

DEBUG = False

ALLOWED_HOSTS = [
    'sisters-demo.herokuapp.com',
    '0.0.0.0'
]
