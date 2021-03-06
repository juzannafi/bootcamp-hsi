import os

# minimum settings.py
SECRET_KEY = 'katasandisayainisusah'
DEBUG = True
ROOT_URLCONF = 'urlsaya'

#Tambahan:
INSTALLED_APPS = [
    'app1'
]

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME' : os.path.join("", 'bootcamp.db')
    }
}

TEMPLATES = [
    {
        'DIRS': ['templates']
    }

]