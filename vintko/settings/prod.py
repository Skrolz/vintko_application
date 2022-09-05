import django_on_heroku
from decouple import config
from .base import *

SECRET_KEY = config('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = [
    'vintko.herokuapp.com',
]

DEBUG_PROPAGATE_EXCEPTIONS = True

django_on_heroku.settings(locals())
