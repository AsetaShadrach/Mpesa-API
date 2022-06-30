from .common import *


DEBUG=config('DEBUG')

ALLOWED_HOSTS = ['*']

LOGIN_URL='/admin/login/'

if DEBUG:
    THIRD_PARTY_APPS = [
    # DEPENDENCIES
    'corsheaders',
    'rest_framework',
    'django_seed',
    'rest_framework_swagger',
    'drf_yasg',
    'oauth2_provider',
    'silk',
    ]
else:
    THIRD_PARTY_APPS = [
    # DEPENDENCIES
    'corsheaders',
    'rest_framework',
    'rest_framework_swagger',
    'drf_yasg',
    'oauth2_provider',
    ]


INSTALLED_APPS.extend(THIRD_PARTY_APPS)
