from .common import *


DEBUG=config('DEBUG')

ALLOWED_HOSTS = ['*']

LOGIN_URL='/admin/login/'

if DEBUG:
    INSTALLED_APPS.append('silk',)
