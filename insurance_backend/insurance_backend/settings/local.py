# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=zqvgkse5#7#l7g09+5+axsq4mgvl8y4fd^ef%yldwekzm@r+1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': "insurance",
        'USER': "root",
        'PASSWORD': "secret",
        'HOST': '127.0.0.1',
                'PORT': 3306
    },
}
