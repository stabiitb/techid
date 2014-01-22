"""
Django settings for events project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
ROOT_DIR = os.path.dirname( os.path.dirname( __file__ ) )
#sudo apt-get install libjpeg62-dev zlib1g-dev libfreetype6-dev liblcms1-dev
#sudo apt-get install libjpeg-dev
WIKI_MARKDOWN_KWARGS = {'extensions': ['footnotes', 'attr_list', 'headerid', 'extra', 'codehilite', ]}
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'vn$-p69z0ea^t5#hzhl*z6xichnl70nbv%$8e=5g6$e#0w@r0t'

USE_TZ = True

# SECURITY WARNING: don't run with debug turned on in production!
#<<<<<<< HEAD

DEBUG = False
REAL_DEBUG = False

#=======
DEBUG = True
REAL_DEBUG = False
#>>>>>>> 37801b7d7ede8da75c24402d749145eab00ef03b
SITE_ID = 1
WIKI_ACCOUNT_HANDLING = False
TEMPLATE_DEBUG = True
FIXTURE_DIRS = (
    ROOT_DIR + "/fixtures/",
    )
ALLOWED_HOSTS = ['techid.stab-iitb.org']
## Added for the suit settings
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
    # "sekizai.context_processors.sekizai",
)

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    ROOT_DIR+'/templates/',
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# Application definition
STATICFILES_DIRS = (
    ROOT_DIR+'/static/',
)
AUTH_USER_MODEL = 'signup.User'                  

STATIC_ROOT = ROOT_DIR + "/staticfiles/"
MEDIA_ROOT = ROOT_DIR+'/media/'
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'suit',
    'django.contrib.admin',
    'event',
    'users',
    'signup',
    'misc',
    'redactor',
    'registration',
    'suit_redactor',
    'bootstrap3',
    'django_select2',
    'projects',
    'endless_pagination',
    'bootstrap3_datetime',
    'tinkerer',
#    'easy_thumbnails',
    'image_cropping',
    'like_button',
    'resources',
    'sorl.thumbnail',
    'calendar_sms',
    'imperavi',
    'newsletter',
    # 'django_tables2',
    # 'south',
    # 'filebrowser',
    # 'django.contrib.humanize',
    # 'django.contrib.sites',
    # 'south',
    # 'django_notify',
    # 'mptt',
    # 'sekizai',
    # 'sorl.thumbnail',
    # 'wiki',
    # 'wiki.plugins.attachments',
    # 'wiki.plugins.notifications',
    # 'wiki.plugins.images',
    # 'wiki.plugins.macros',
)


REDACTOR_OPTIONS = {'lang': 'en'}
REDACTOR_UPLOAD = 'uploads/'

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'events.urls'

WSGI_APPLICATION = 'events.wsgi.application'

NEWSLETTER_RICHTEXT_WIDGET = "imperavi.widget.ImperaviWidget"
# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
if REAL_DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'OPTIONS': {
                'read_default_file': '/var/www/event/database.conf',
            },
        }
        }

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Calcutta'

USE_I18N = True

USE_L10N = True



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/uploads/'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
if REAL_DEBUG:
# Host for sending e-mail.
    EMAIL_HOST = 'localhost'

    # Port for sending e-mail.
    EMAIL_PORT = 1025
else:
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_PORT =  587
    # Optional SMTP authentication information for EMAIL_HOST.
    EMAIL_HOST_USER = 'stab.iitb@gmail.com'
    EMAIL_HOST_PASSWORD = 'stab2011'
    EMAIL_USE_TLS = True

BLEACH_VALID_TAGS = ['p', 'b', 'i', 'strike', 'ul', 'li', 'ol', 'br',
                     'span', 'blockquote', 'hr', 'a', 'img','div','h1','h2','h3',
                     'h4','h5','h6','dd','dl','em']
BLEACH_VALID_ATTRS = {
    'span': ['style', ],
    'p': ['align', ],
    'a': ['href', 'rel'],
    'img': ['src', 'alt', 'style'],
}
BLEACH_VALID_STYLES = ['color', 'cursor', 'float', 'margin']

from easy_thumbnails.conf import Settings as thumbnail_settings
THUMBNAIL_PROCESSORS = (
    'image_cropping.thumbnail_processors.crop_corners',
) + thumbnail_settings.THUMBNAIL_PROCESSORS

IMAGE_CROPPING_SIZE_WARNING = True

JQUERY_URL = "/static/jquery.js"

FACEBOOK_APP_ID = "714398431904909"
FACEBOOK_SHOW_SEND = "true"   # or "false, default is "true"
FACEBOOK_LIKE_WIDTH = "450"   # "numeric value for width", default is 450
FACEBOOK_SHOW_FACES = "true"  # or "false, default is "true"

