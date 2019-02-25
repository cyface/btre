from .settings import *

ALLOWED_HOSTS = ['dev.cyface.com', 'btre.cyface.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'btre',
        'USER': 'btre',
        'PASSWORD': 'btre123',
        'HOST': 'database',
        'PORT': '5432',
    }
}
