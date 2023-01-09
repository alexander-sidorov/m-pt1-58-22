import os
from pathlib import Path

DIR_REPO = Path(__file__).parent.parent.resolve()


SECRET_KEY = os.getenv("APP_SECRET_KEY") or "1"


DEBUG = True


ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
]


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "app_alexander_sidorov",
    "app_dmitry_mikhailiuk",
    "app_jana_sergienko",
    "app_eugene_lubimov",
    "app_vadim_zharski",
    "app_vladislav_yurenya",
]


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


ROOT_URLCONF = "project.urls"


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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


WSGI_APPLICATION = "project.wsgi.application"


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": DIR_REPO / "db.sqlite3",
    }
}


_pv = "django.contrib.auth.password_validation"

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": f"{_pv}.UserAttributeSimilarityValidator",
    },
    {
        "NAME": f"{_pv}.MinimumLengthValidator",
    },
    {
        "NAME": f"{_pv}.CommonPasswordValidator",
    },
    {
        "NAME": f"{_pv}.NumericPasswordValidator",
    },
]


LANGUAGE_CODE = "en-us"


TIME_ZONE = "UTC"


USE_I18N = True


USE_TZ = True


STATIC_URL = "static/"


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
