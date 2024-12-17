from dotenv import dotenv_values
from config.settings.base import *

ENV = dotenv_values('../../envs/.env.prod')

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ENV['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ENV['ALLOWED_HOSTS'].split(', ')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'
