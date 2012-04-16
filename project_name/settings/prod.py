"""Production settings and globals."""


from os import environ
from sys import exc_info
from urlparse import urlparse, uses_netloc

from S3 import CallingFormat

from common import config



########## EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/1.3/ref/settings/#email-backend
config['EMAIL_BACKEND'] = 'django.core.mail.backends.smtp.EmailBackend'

# See: https://docs.djangoproject.com/en/1.3/ref/settings/#email-host
config['EMAIL_HOST'] = environ.get('EMAIL_HOST', 'smtp.gmail.com')

# See: https://docs.djangoproject.com/en/1.3/ref/settings/#email-host-password
config['EMAIL_HOST_PASSWORD'] = environ.get('EMAIL_HOST_PASSWORD', '')

# See: https://docs.djangoproject.com/en/1.3/ref/settings/#email-host-user
config['EMAIL_HOST_USER'] = environ.get('EMAIL_HOST_USER',
                                        'your_email@example.com')

# See: https://docs.djangoproject.com/en/1.3/ref/settings/#email-port
config['EMAIL_PORT'] = environ.get('EMAIL_PORT', 587)

# See: https://docs.djangoproject.com/en/1.3/ref/settings/#email-subject-prefix
config['EMAIL_SUBJECT_PREFIX'] = '[%s] ' % config['SITE_NAME']

# See: https://docs.djangoproject.com/en/1.3/ref/settings/#email-use-tls
config['EMAIL_USE_TLS'] = True

# See: https://docs.djangoproject.com/en/1.3/ref/settings/#server-email
config['SERVER_EMAIL'] = config['EMAIL_HOST_USER']
########## END EMAIL CONFIGURATION


########## DATABASE CONFIGURATION
# See: http://devcenter.heroku.com/articles/django#postgres_database_config
uses_netloc.append('postgres')
uses_netloc.append('mysql')
uses_netloc.append('oracle')
engine_mapping = {'postgres':'django.db.backends.postgresql_psycopg2',
                  'mysql':'django.db.backends.mysql',
                  'oracle':'django.db.backends.oracle'}

try:
    url = environ.get('DATABASE_URL')
    if not url is None:
        url = urlparse(url)
        config['DATABASES']['default'] = {
            'NAME': url.path[1:],
            'USER': url.username,
            'PASSWORD': url.password,
            'HOST': url.hostname,
            'PORT': url.port,
            'ENGINE': engine_mapping[url.scheme],
        }
except:
    print "Unexpected error:", exc_info()
########## END DATABASE CONFIGURATION


########## CACHE CONFIGURATION
# See: https://docs.djangoproject.com/en/1.3/ref/settings/#caches
config['CACHES'] = {
    'default': {
        'BACKEND': 'django_pylibmc.memcached.PyLibMCCache',
        'LOCATION': 'localhost:11211',
        'TIMEOUT': 500,
        'BINARY': True,
        'OPTIONS': {
            'tcp_nodelay': True,
            'ketama': True,
        }
    }
}
########## END CACHE CONFIGURATION


########## CELERY CONFIGURATION
# See: http://docs.celeryproject.org/en/latest/configuration.html#broker-transport
config['BROKER_TRANSPORT'] = 'amqplib'

# See: http://docs.celeryproject.org/en/latest/configuration.html#broker-url
config['BROKER_URL'] = environ.get('RABBITMQ_URL', '')

# See: http://docs.celeryproject.org/en/latest/configuration.html#celery-result-backend
config['CELERY_RESULT_BACKEND'] = 'amqp'

# See: http://docs.celeryproject.org/en/latest/configuration.html#celery-task-result-expires
config['CELERY_TASK_RESULT_EXPIRES'] = 60 * 60 * 5
########## END CELERY CONFIGURATION


########## STORAGE CONFIGURATION
# See: http://django-storages.readthedocs.org/en/latest/index.html
config['INSTALLED_APPS'] += (
    'storages',
)

# See: http://django-storages.readthedocs.org/en/latest/backends/amazon-S3.html#settings
config['DEFAULT_FILE_STORAGE'] = 'storages.backends.s3boto.S3BotoStorage'
config['STATICFILES_STORAGE'] = 'storages.backends.s3boto.S3BotoStorage'

config['AWS_CALLING_FORMAT'] = CallingFormat.SUBDOMAIN

config['AWS_ACCESS_KEY_ID'] = environ.get('AWS_ACCESS_KEY_ID', '')
config['AWS_SECRET_ACCESS_KEY'] = environ.get('AWS_SECRET_ACCESS_KEY', '')
config['AWS_STORAGE_BUCKET_NAME'] = environ.get('AWS_STORAGE_BUCKET_NAME', '')

config['STATIC_URL'] = ('https://s3.amazonaws.com/%s/' %
                        config['AWS_STORAGE_BUCKET_NAME'])
########## END STORAGE CONFIGURATION


########## WEBSERVER CONFIGURATION
# See: http://gunicorn.org/
config['INSTALLED_APPS'] += (
    'gunicorn',
)
########## END WEBSERVER CONFIGURATION
