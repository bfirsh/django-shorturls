import os

DEBUG = TEMPLATE_DEBUG = True
SECRET_KEY = '123'

# For Pre-Django 1.3
DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = '/tmp/shorturls.db'

# For Django 1.3 and beyond
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3'
    }
}

INSTALLED_APPS = ['shorturls']
ROOT_URLCONF = ['shorturls.urls']
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
    },
]
