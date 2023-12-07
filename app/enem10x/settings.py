"""
Django settings for enem10x project.

Generated by 'django-admin startproject' using Django 4.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
from os import getenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR.parent / "data"

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key usqed in production secret!
SECRET_KEY = str(
    getenv(
        "SECRET_KEY",
        "2cx(t4hbv03a2m_0i7pt*jr%n50ql9m3scs8eklovm=t)!t&-4",
    )
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(int(getenv("DEBUG", default=1)))

ALLOWED_HOSTS = [h.strip() for h in getenv("ALLOWED_HOSTS", "").split(",") if h.strip()]


# Application definition

INSTALLED_APPS = [
    # jazzmin plugin
    "jazzmin",
    # django default
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # onw
    "debug_toolbar",
    "materiais",
    "provas",
    "usuarios",
    "home",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "enem10x.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "enem10x.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases


# postgress

DATABASES = {
    "default": {
        "ENGINE": getenv("DB_ENGINE"),
        "NAME": getenv("POSTGRES_DB"),
        "USER": getenv("POSTGRES_USER"),
        "PASSWORD": getenv("POSTGRES_PASSWORD"),
        "HOST": getenv("POSTGRES_HOST"),
        "PORT": getenv("POSTGRES_PORT"),
        "TEST": {"NAME": "test"},
    },
    "replica": {
        "ENGINE": getenv("DB_ENGINE"),
        "NAME": getenv("POSTGRES_DB"),
        "USER": getenv("POSTGRES_REPLICATION_USER"),
        "PASSWORD": getenv("POSTGRES_REPLICATION_PASSWORD"),
        "HOST": getenv("POSTGRES_HOST_REPLICATION_1"),
        "PORT": getenv("POSTGRES_PORT"),
        "TEST": {"MIRROR": "default"},
    },
}

DATABASE_ROUTERS = ["enem10x.routers.Router"]

# sqlite3
"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',

    }
}
"""


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "pt-br"

TIME_ZONE = "America/Sao_Paulo"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = DATA_DIR / "static"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# Changing the user model

AUTH_USER_MODEL = "usuarios.Account"

# Login url to login_required decorator

LOGIN_URL = "/usuarios/login"

# DEFINE O ARMAZENAMENTO DE SESSAO COMO PADRAO NO BANCO DE DADOS E TEMPO EM SEGUNDOS PARA TIMEOUT AUTOMATICO
SESSION_ENGINE = "django.contrib.sessions.backends.db"
SESSION_COOKIE_AGE = 604800  # 1 semana


# Define local para armezanemto de medias

MEDIA_URL = "/data/media/"
MEDIA_ROOT = DATA_DIR / "media"

# admin panel plugin settings
JAZZMIN_SETTINGS = {
    "site_title": "Enem 10x admin",
    "site_header": "Enem 10x admin",
    "site_brand": "Enem 10x",
    "site_icon": "home/enem10xlogo.png",
    "login_logo": "home/enem10xlogo.png",
    "site_logo": "home/enem10xlogo.png",
    "welcome_sign": "Enem 10x admin",
    "copyright": "Enem 10x",
    "changeform_format": "vertical_tabs",
}


# CELERY -> REDIS


CELERY_BROKER_URL = "redis://redis:6379"
CELERY_RESULT_BACKEND = "redis://redis:6379"


# Fake cache for DEV
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.dummy.DummyCache",
    }
}


# Real cache for PROD
"""CACHES = {
    "default":{
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": CELERY_BROKER_URL,
        "OPTIONS": {
            "CLIENT_CLASS":"django_redis.client.DefaultClient",
        }
    }
}"""

# The Debug Toolbar is shown only if your IP address is listed in Django’s INTERNAL_IPS setting.
# This means that for local development, you must add "127.0.0.1" to
# INTERNAL_IPS. You’ll need to create this setting if it doesn’t already exist in your settings module:
# Internal ips

if DEBUG:
    import socket  # only if you haven't already imported this

    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS = [ip[: ip.rfind(".")] + ".1" for ip in ips] + [
        "127.0.0.1",
        "10.0.2.2",
    ]
