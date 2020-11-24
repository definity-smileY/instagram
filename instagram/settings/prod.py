from .base import *

# export DJANGO_SETTINGS_MODULE=instagram.settings.prod
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR , 'db.sqlite3'),
    }
}

DEBUG = False