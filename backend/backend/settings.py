import os
from pathlib import Path
import environ
from datetime import timedelta


env = environ.Env()

environ.Env.read_env(".env")

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = env("SECRET_KEY")

# SECRET_KEY = 'django-insecure-a09yb##f=m$-i&9t0)&de_5_^6vjpqn6%1z+v$d^$4j5_d--fn'

DEBUG = True

ALLOWED_HOSTS = ["todos-latest-u3mg.onrender.com"]

CSRF_TRUSTED_ORIGINS = ['https://todos-latest-u3mg.onrender.com']

INSTALLED_APPS = [
    'base',
    'tailwind',
    'theme',
    'todos',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

NPM_BIN_PATH = r"C:\Program Files\nodejs\npm.cmd"

if DEBUG:
    # Add django_browser_reload only in DEBUG mode
    INSTALLED_APPS += ['django_browser_reload']

TAILWIND_APP_NAME = 'theme'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

if DEBUG:
    MIDDLEWARE += [
        "django_browser_reload.middleware.BrowserReloadMiddleware",
    ]

ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'backend.wsgi.application'

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env("COMMON_DB_NAME"),
        'USER': env("COMMON_DB_USERNAME"),
        'PASSWORD': env("COMMON_DB_PASSWORD"),
        'HOST': env("COMMON_DB_HOST"),
        'PORT': env("COMMON_DB_PORT"),
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / "static",  # Your global static folder
]

STATIC_ROOT = BASE_DIR / "staticfiles"  # Where collectstatic stores files

# Media files (User-uploaded content)
MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR / "media"

# ✅ Required for Django 4.2+ storage handling
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",  # for media uploads
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}
