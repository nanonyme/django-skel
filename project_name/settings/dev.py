"""Development settings and globals."""


from os.path import join, normpath

from common import config


########## DEBUG CONFIGURATION
# See: https://docs.djangoproject.com/en/1.3/ref/settings/#debug
config['DEBUG'] = True

# See: https://docs.djangoproject.com/en/1.3/ref/settings/#template-debug
config['TEMPLATE_DEBUG'] = config['DEBUG']
########## END DEBUG CONFIGURATION


########## EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/1.3/ref/settings/#email-backend
config['EMAIL_BACKEND'] = 'django.core.mail.backends.console.EmailBackend'
########## END EMAIL CONFIGURATION


########## DATABASE CONFIGURATION
# See: https://docs.djangoproject.com/en/1.3/ref/settings/#databases
config['DATABASES'] = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': normpath(join(config['DJANGO_ROOT'], 'default.db')),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}
########## END DATABASE CONFIGURATION


########## CACHE CONFIGURATION
# See: https://docs.djangoproject.com/en/1.3/ref/settings/#caches
config['CACHES'] = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}
########## END CACHE CONFIGURATION


########## CELERY CONFIGURATION
# See: http://ask.github.com/django-celery/
config['INSTALLED_APPS'] += (
    'djkombu',
)

# See: http://docs.celeryq.org/en/latest/configuration.html#broker-transport
config['BROKER_TRANSPORT'] = 'djkombu.transport.DatabaseTransport'

# See: http://docs.celeryq.org/en/latest/configuration.html#celery-result-dburi
config['CELERY_RESULT_DBURI'] = config['DATABASES']['default']

# See: http://docs.celeryq.org/en/latest/configuration.html#celery-always-eager
config['CELERY_ALWAYS_EAGER'] = True
########## END CELERY CONFIGURATION
