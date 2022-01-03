from .base import env

# DJANGO DEVELOPMENT SECRET KEY
SECRET_KEY = 'django-insecure-=o@21n9jl8ik)zm3bssh7j$&1c4cy#vve934y!9=5joe0q5d4n'

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': '127.0.0.1',
        'PORT': '5432',
        'TEST': {
            'NAME': 'test_db'
        },
    }
}

