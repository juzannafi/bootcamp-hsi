import os

SECRET_KEY ='password'
DEBUG = True
ROOT_URLCONF = 'tools.urls'

INSTALLED_APPS = [
    'app',
    # 'tools'
    # 'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    # 'django.contrib.sessions',
    # 'django.contrib.messages',
    # 'django.contrib.staticfiles',
]

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join("", 'peserta.db')
    }
}
#
# MIDDLEWARE = [
#     # 'django.middleware.security.SecurityMiddleware',
#     # 'django.contrib.sessions.middleware.SessionMiddleware',
#     # 'django.middleware.common.CommonMiddleware',
#     # 'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
# ]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [''],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]