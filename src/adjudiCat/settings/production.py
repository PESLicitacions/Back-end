from adjudiCat.settings.common import *
import environ
# SECURITY WARNING: keep the secret key used in production secret!
env = environ.Env(  # <-- Updated!
    # set casting, default value
    DEBUG=(bool, False),
)

environ.Env.read_env(BASE_DIR / '.env')

SECRET_KEY = env('SECRET_KEY')


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Opcions per el deploy
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True

CSRF_TRUSTED_ORIGINS = ['https://*.fib.upc.edu:40410']

ALLOWED_HOSTS = ['0.0.0.0','nattech.fib.upc.edu',]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env('MYSQL_DATABASE'),
        'USER':  env('MYSQL_USER'),
        'PASSWORD':  env('MYSQL_PASSWORD'),
        'HOST':  env('MYSQL_DATABASE_HOST'),
        'PORT':  env('MYSQL_DATABASE_PORT'),
    }
}