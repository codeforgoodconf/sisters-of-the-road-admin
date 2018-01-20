"""
Settings module for sistersadmin

For more information on Django config, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/

We use a separate file for each environment. 
Each should import common settings from base.py

Config secrets are stored in environmnet variables

Required environment variables:
DJANGO_SETTINGS_MODULE: sistersadmin.settings.[environment name]
DJANGO_SECRET_KEY: # required for anything but dev
DATABASE_URL: # required for heroku
"""
