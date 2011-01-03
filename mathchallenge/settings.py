import os

# Setup the project and media root according to the current file 
PROJECT_ROOT = os.path.dirname(__file__)
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')

# Media and admin media should be standard as noted below
MEDIA_URL = '/media/'

# Setup the admins that get code error notifications when 
# debug is false. Also setup managers which will send out 
# notifications when broken links exist (or for general 
# purpose e-mail notifications)
ADMINS = (('', ''),)
MANAGERS = ADMINS

# Setup the secondary requirements for the site_id
# root url conf to urls (since we will start from the project 
# on the path), language will be in english and we will not use 
# internationalization.
SITE_ID = 1
ROOT_URLCONF = 'urls'
TIME_ZONE = 'America/New_York'
LANGUAGE_CODE = 'en-us'
USE_I18N = True
SECRET_KEY = 'q+ip=icq$d2a1(rr@dqz(&45r@&=*+dxv*4kb3&%pj%p)rvg'

# Set the default caching on a 120 minimum interval
CACHE_MIDDLEWARE_SECONDS = 120
CACHE_MIDDLEWARE_KEY_PREFIX = 'mathch'
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'

# Setup all the different template processors, loaders, middleware
# template dirs and all the installed applications.
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.media',
    'django.core.context_processors.request',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.gzip.GZipMiddleware',
    #'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    #'django.middleware.cache.FetchFromCacheMiddleware',
)

TEMPLATE_DIRS = (os.path.join(PROJECT_ROOT, 'templates'),)
INSTALLED_APPS = (
    # Setup the default installed apps (native to most django apps)
    'django.contrib.sessions',

    # Add extensions and debugging capabilities
    'django_extensions',

    # Add third party dependency apps to handle various features
)

try:
    LOCAL_SETTINGS
except NameError:
    try:
        from local_settings import *
    except ImportError:
        pass
