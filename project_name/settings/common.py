"""Common settings and globals."""

from django import conf

from datetime import timedelta
from os.path import abspath, basename, dirname, join, normpath

from djcelery import setup_loader
config = {}

class DictWrapper(object):
    def __init__(self, wrapped):
        wrapped.update(self.__dict__)
        self.__dict__ = wrapped

conf.settings = conf.LazySettings()
conf.settings.configure(default_settings=DictWrapper(config))


#settings.configure(default_settings=config)

########## PATH CONFIGURATION
# Absolute filesystem path to the Django project directory:
config['DJANGO_ROOT'] = dirname(dirname(abspath(__file__)))

# Absolute filesystem path to the top-level project folder:
config['SITE_ROOT'] = dirname(config['DJANGO_ROOT'])

# Site name:
config['SITE_NAME'] = basename(config['DJANGO_ROOT'])
########## END PATH CONFIGURATION


########## DEBUG CONFIGURATION
# See: https://docs.djangoproject.com/en/1.3/ref/settings/#debug
config['DEBUG'] = False

# See: https://docs.djangoproject.com/en/1.3/ref/settings/#template-debug
config['TEMPLATE_DEBUG'] = config['DEBUG']
########## END DEBUG CONFIGURATION


########## MANAGER CONFIGURATION
# See: https://docs.djangoproject.com/en/1.3/ref/settings/#admins
config['ADMINS'] = (
    ('Your Name', 'your_email@example.com'),
)

# See: https://docs.djangoproject.com/en/1.3/ref/settings/#managers
config['MANAGERS'] = config['ADMINS']
########## END MANAGER CONFIGURATION


########## DATABASE CONFIGURATION
# See: https://docs.djangoproject.com/en/1.3/ref/settings/#databases
config['DATABASES'] = {
    'default': {
        'ENGINE': 'django.db.backends.',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}
########## END DATABASE CONFIGURATION


########## GENERAL CONFIGURATION
# See: https://docs.djangoproject.com/en/1.3/ref/settings/#time-zone
config['TIME_ZONE'] = 'America/Los_Angeles'

# See: https://docs.djangoproject.com/en/1.3/ref/settings/#language-code
config['LANGUAGE_CODE'] = 'en-us'

# See: https://docs.djangoproject.com/en/1.3/ref/settings/#site-id
config['SITE_ID'] = 1

# See: https://docs.djangoproject.com/en/1.3/ref/settings/#use-i18n
config['USE_I18N'] = True

# See: https://docs.djangoproject.com/en/1.3/ref/settings/#use-l10n
config['USE_L10N'] = True
########## END GENERAL CONFIGURATION


########## MEDIA CONFIGURATION
# See: https://docs.djangoproject.com/en/1.3/ref/settings/#media-root
config['MEDIA_ROOT'] = normpath(join(config['DJANGO_ROOT'], 'media'))

# See: https://docs.djangoproject.com/en/1.3/ref/settings/#media-url
config['MEDIA_URL'] = '/media/'
########## END MEDIA CONFIGURATION


########## STATIC FILE CONFIGURATION
# See: https://docs.djangoproject.com/en/1.3/ref/settings/#static-root
config['STATIC_ROOT'] = normpath(join(config['DJANGO_ROOT'], 'static'))

# See: https://docs.djangoproject.com/en/1.3/ref/settings/#static-url
config['STATIC_URL'] = '/static/'

# See: https://docs.djangoproject.com/en/1.3/ref/settings/#admin-media-prefix
config['ADMIN_MEDIA_PREFIX'] = '/static/admin/'

# See: https://docs.djangoproject.com/en/1.3/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
config['STATICFILES_DIRS'] = (
    normpath(join(config['DJANGO_ROOT'], 'assets')),
)

# See: https://docs.djangoproject.com/en/1.3/ref/contrib/staticfiles/#staticfiles-finders
config['STATICFILES_FINDERS'] = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
########## END STATIC FILE CONFIGURATION


########## AJAX CONFIGURATION
# See: http://docs.dajaxproject.com/dajaxice/available-settings.html#dajaxice-media-prefix
config['DAJAXICE_MEDIA_PREFIX'] = 'dajaxice'
########## END AJAX CONFIGURATION


########## SECRET CONFIGURATION
# See: https://docs.djangoproject.com/en/1.3/ref/settings/#secret-key
config['SECRET_KEY'] = r"{{ secret_key }}"
########## END SECRET CONFIGURATION


########## FIXTURE CONFIGURATION
# See: https://docs.djangoproject.com/en/1.3/ref/settings/#std:setting-FIXTURE_DIRS
config['FIXTURE_DIRS'] = (
    normpath(join(config['DJANGO_ROOT'], 'fixtures')),
)
########## END FIXTURE CONFIGURATION


########## TEMPLATE CONFIGURATION
# See: https://docs.djangoproject.com/en/1.3/ref/settings/#template-context-processors
config['TEMPLATE_CONTEXT_PROCESSORS'] = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages'
)

# See: https://docs.djangoproject.com/en/1.3/ref/settings/#template-loaders
config['TEMPLATE_LOADERS'] = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

# See: https://docs.djangoproject.com/en/1.3/ref/settings/#template-dirs
config['TEMPLATE_DIRS'] = (
    normpath(join(config['DJANGO_ROOT'], 'templates')),
)
########## END TEMPLATE CONFIGURATION


########## MIDDLEWARE CONFIGURATION
# See: https://docs.djangoproject.com/en/1.3/ref/settings/#middleware-classes
config['MIDDLEWARE_CLASSES'] = (
    # Use GZip compression to reduce bandwidth.
    'django.middleware.gzip.GZipMiddleware',

    # Minify all HTML when DEBUG is False.
    'htmlmin.middleware.HtmlMinifyMiddleware',

    # Default Django middleware.
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)
########## END MIDDLEWARE CONFIGURATION


########## URL CONFIGURATION
# See: https://docs.djangoproject.com/en/1.3/ref/settings/#root-urlconf
config['ROOT_URLCON'] = '%s.urls' % config['SITE_NAME']
########## END URL CONFIGURATION


########## APP CONFIGURATION
DJANGO_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Useful template tags:
    'django.contrib.humanize',

    # Admin panel and documentation:
    'django.contrib.admin',
    'django.contrib.admindocs',
)

THIRD_PARTY_APPS = (
    # Database migration helpers:
    'south',

    # AJAX helpers:
    'dajaxice',

    # Asynchronous task queue:
    'djcelery',
)

LOCAL_APPS = (
)

# See: https://docs.djangoproject.com/en/1.3/ref/settings/#installed-apps
config['INSTALLED_APPS'] = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
########## END APP CONFIGURATION


########## LOGGING CONFIGURATION
# See: https://docs.djangoproject.com/en/1.3/ref/settings/#logging
config['LOGGING'] = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
########## END LOGGING CONFIGURATION


########## CELERY CONFIGURATION
# See: http://celery.readthedocs.org/en/latest/configuration.html#celery-task-result-expires
config['CELERY_TASK_RESULT_EXPIRES'] = timedelta(minutes=30)

# See: http://ask.github.com/django-celery/
setup_loader()
########## END CELERY CONFIGURATION
