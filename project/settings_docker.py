from .settings import *

ALLOWED_HOSTS = ['127.0.0.1', 'dev.cyface.com', 'btre.cyface.com']

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://redis',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient'
        }
    }
}

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
