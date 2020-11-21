import os

SECRET_KEY = 'katasandisayainisusah'
DEBUG = True
ROOT_URLCONF = 'urlsaya'

INSTALLED_APPS = [
    'app1',
]

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join("", 'bootcamp.db'),
    },
    'db_hsi': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'tifa.db'),
    },
    'db_pernik': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'tifa.db'),
    },
}
