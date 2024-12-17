import os

from dotenv import dotenv_values
from config.settings.base import *

ENV = dotenv_values(BASE_DIR / 'envs/.env.prod')

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ENV['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ENV['ALLOWED_HOSTS'].split(', ')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': ENV.get('POSTGRES_HOST', 'localhost'),
        'NAME': ENV.get('POSTGRES_DBNAME', 'oz_practice'),
        'USER': ENV.get('POSTGRES_USER', 'postgres'),
        'PASSWORD': ENV.get('POSTGRES_PASSWORD', 'postgres'),
        'PORT': ENV.get('POSTGRES_PORT', 5432),
    }
}

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, '.staticfiles')
