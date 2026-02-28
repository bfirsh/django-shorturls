DEBUG = True
SECRET_KEY = '123'
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3'
    }
}

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

INSTALLED_APPS = ['shorturls']
ROOT_URLCONF = 'shorturls.urls'

SHORTEN_MODELS = {
    'A': 'shorturls.animal',
    'V': 'shorturls.vegetable',
    'M': 'shorturls.mineral',
}
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
    },
]
