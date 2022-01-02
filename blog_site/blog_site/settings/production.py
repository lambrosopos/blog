from .base import env

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-=o@21n9jl8ik)zm3bssh7j$&1c4cy#vve934y!9=5joe0q5d4n'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST'),
        'PORT': env('DB_PORT'),
        'TEST': {
            'NAME': 'test_db'
        },
    }
}
