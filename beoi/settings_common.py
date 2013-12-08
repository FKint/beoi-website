"""
Django settings for beoi project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""
import os
from datetime import datetime
from django.utils.translation import ugettext_lazy as _
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

REGISTRATION_DEADLINE = datetime(2013,11,25,23,59,59)
SEMIFINAL_START = datetime(2013,11,27,14,30,00)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# Make this unique, and don't share it with anybody. To generate a new one, run this in the python console:
# import string
# from random import choice
# print ''.join([choice(string.letters + string.digits + string.punctuation) for i in range(50)])
SECRET_KEY = '__dummy__'

DEBUG = True
TEMPLATE_DEBUG = DEBUG

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'beoi/templates'),
)

ALLOWED_HOSTS = ['.be-oi.be']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' # email to console for dev
SEND_BROKEN_LINK_EMAILS = True # sent mail warning for 404 errors
EMAIL_SUBJECT_PREFIX = '[beOI Django] '

IGNORABLE_404_URLS = (
    re.compile(r'^/cgi-bin/'),
    re.compile(r'\.php$'),
    re.compile(r'\.cgi$'),
    re.compile(r'\.pl$'),
    '/favicon.ico',
)

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'beoi.news',
    'beoi.contest',
    'beoi.faq'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_LOADERS = (
    'beoi.core.TranslatedTemplateLoader',
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader'
)

ROOT_URLCONF = 'beoi.urls'

WSGI_APPLICATION = 'beoi.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'fr'
LANGUAGES = (
  ('fr', _('French')),
  ('nl', _('Dutch')),
)
LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'beoi/locale'),
)

TIME_ZONE = 'Europe/Brussels'
USE_I18N = True
USE_L10N = True
USE_TZ = True



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "beoi/static"),
)