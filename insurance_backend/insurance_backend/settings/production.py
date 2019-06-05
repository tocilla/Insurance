import os
from django.core.exceptions import ImproperlyConfigured


def get_env_var(var_name):
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = f"Set the {var_name} environment variable"
        raise ImproperlyConfigured(error_msg)


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_env_var("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': get_env_var('MYSQL_DB'),
        'USER': get_env_var('MYSQL_USER'),
        'PASSWORD': get_env_var('MYSQL_PASSWORD'),
        'HOST': get_env_var('MYSQL_HOST'),
        'PORT': get_env_var('MYSQL_PORT')
    },
}

ALLOWED_HOSTS = get_env_var('ALLOWED_HOSTS').split(';')
