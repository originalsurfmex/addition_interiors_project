"""
Django settings for addition_interiors_project project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from django.conf import settings
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1s&a^j^cd!7)@%%f$t_c0a@4&jk&+i$dlrmh2-#2c(8nqkab4*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'grappelli',
    'filebrowser',
    # 'suit',
    # 'djangocms_admin_style',
    # 'admin_shortcuts',
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'debug_toolbar',
    'frontpage',
    # adding south to try out with django 1.6
    'south',
    'inplaceeditform',
)

MIDDLEWARE_CLASSES = (
    # FOR DJANGO-DEBUG-TOOLBAR
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'addition_interiors_project.urls'

WSGI_APPLICATION = 'addition_interiors_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# STATIC_ROOT = '/var/www/static'
# MEDIA_ROOT = '/var/www/media'

# GRAPPELLI and Django-Suit SPECIFIC RECOMMENDED ##
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.request",
    # MY CUSTOM TEMPLATE PROCESSORS
    "frontpage.context_processors.base_page",
    # SERVE UP MEDIA FILES
    "django.core.context_processors.media",
)


#FOR DJANGO DEBUG TOOLBAR
def show_toolbar(request):
    return True
SHOW_TOOLBAR_CALLBACK = show_toolbar

INTERNAL_IPS = ('127.0.0.1', '192.168.0.1',)

DEBUG_TOOLBAR_CONFIG = {'INTERCEPT_REDIRECTS': False,}


#DEBUG_TOOLBAR_PATCH_SETTINGS = True

#-------------------------------------------------------------
# FRONT END EDITING
#-------------------------------------------------------------
INPLACEEDIT_EDIT_EMPTY_VALUE = 'Double click to edit'
INPLACEEDIT_AUTO_SAVE = True
INPLACEEDIT_EVENT = "dblclick"
INPLACEEDIT_DISABLE_CLICK = True  # For inplace edit text into a link tag
# INPLACEEDIT_EDIT_MESSAGE_TRANSLATION = 'Write a translation' # transmeta
# option
INPLACEEDIT_SUCCESS_TEXT = 'Successfully saved'
INPLACEEDIT_UNSAVED_TEXT = 'You have unsaved changes'
INPLACE_ENABLE_CLASS = 'enable'
# DEFAULT_INPLACE_EDIT_OPTIONS = {} # dictionnary of the optionals parameters that the templatetag can receive to change its behavior (see the Advanced usage section)
# DEFAULT_INPLACE_EDIT_OPTIONS_ONE_BY_ONE = True # modify the behavior of the DEFAULT_INPLACE_EDIT_OPTIONS usage, if True then it use the default values not specified in your template, if False it uses these options only when the dictionnary is empty (when you do put any options in your template)
# ADAPTOR_INPLACEEDIT_EDIT = 'app_name.perms.MyAdaptorEditInline' # Explain in Permission Adaptor API
# ADAPTOR_INPLACEEDIT = {'myadaptor': 'app_name.fields.MyAdaptor'} #
# Explain in Adaptor API
# to change the url where django-inplaceedit use to get a field
INPLACE_GET_FIELD_URL = None
# to change the url where django-inplaceedit use to save a field
INPLACE_SAVE_URL = None


#-------------------------------------------------------------
# send_mail
#-------------------------------------------------------------
EMAIL_HOST = "smtp.gmail.com"
EMAIL_HOST_USER = "xxxxxxxxxx@gmail.com"
EMAIL_HOST_PASSWORD = 'xxxxxxxxxx'
EMAIL_PORT = 587
EMAIL_USE_TLS = True


#-------------------------------------------------------------
# DJANGO-FILEBROWSER
#-------------------------------------------------------------

FILEBROWSER_VERSIONS_BASEDIR = '_versions'
FILEBROWSER_VERSIONS = {
  'admin_thumbnail': {'verbose_name': 'Admin Thumbnail', 'width': 60, 'height': 60, 'opts': 'crop'},
  'thumbnail': {'verbose_name': 'Thumbnail (1 col)', 'width': 60, 'height': 60, 'opts': 'crop'},
  'small': {'verbose_name': 'Small (2 col)', 'width': 140, 'height': '', 'opts': ''},
  'medium': {'verbose_name': 'Medium (4col )', 'width': 300, 'height': '', 'opts': ''},
  'big': {'verbose_name': 'Big (6 col)', 'width': 460, 'height': '', 'opts': ''},
  'large': {'verbose_name': 'Large (8 col)', 'width': 680, 'height': '', 'opts': ''},
  'mega': {'verbose_name': 'Mega (12 col)', 'width': 940, 'height': '', 'opts': ''},
}

FILEBROWSER_ADMIN_VERSIONS = getattr(settings, 'FILEBROWSER_ADMIN_VERSIONS', ['thumbnail', 'small', 'medium', 'big', 'large', 'mega'])