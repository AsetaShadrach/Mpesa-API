from .common import *


DEBUG=config('DEBUG')

ALLOWED_HOSTS = ['*']

if DEBUG:
    INSTALLED_APPS.append('silk',)
