import os

SECRET_KEY ='password'
DEBUG = True
ROOT_URLCONF = 'tools.urls'

INSTALLED_APPS = [
    'app'
]

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME' : os.path.join("", 'peserta.db')
    }
}