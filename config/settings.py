"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 3.2.8.
Current Django Version: See Pipfile.lock

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os

# For getting Environment Variables
# --- Snip from "Two Scoops of Django" ---
# Normally you should not import ANYTHING from Django directly
# into your settings, but ImproperlyConfigured is an exception.
from django.core.exceptions import ImproperlyConfigured


def get_env_variable(var_name):
    """Get the environment variable or return exception."""
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = f"Set the {var_name} environment variable"
        raise ImproperlyConfigured(error_msg)


# --- End Snip ---
def string_int_to_int(var):
    """Convert strings of integers to integers, but keep all other types the same."""
    try:
        return int(var)
    except ValueError:
        return var


# End 'For Environment Variables'

# Determine environment
ENV = get_env_variable("ENV")

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_env_variable("DJANGO_SECRET_KEY")


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(int(get_env_variable("DJANGO_DEBUG")))

ALLOWED_HOSTS = ["localhost", "127.0.0.1", ".herokuapp.com"]

INTERNAL_IPS = [
    "127.0.0.1",
    "0.0.0.0"  # Added for Django Debug Toolbar
]

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    # Third-party apps
    "whitenoise.runserver_nostatic",  # Tells Django to use 'whitenoise' in development rather than Django default.
    "django.contrib.staticfiles",
    # Local apps
    "accounts",
    "main",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # Tells Django where to find templates outside of apps.
        "DIRS": [
            BASE_DIR / "templates",
        ],
        # Tells Django to serch for templates in apps.
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

WSGI_APPLICATION = "config.wsgi.application"

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

if ENV == "TEST":
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": ":memory:",  # OR 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
elif ENV == "DEV":
    # Database setting for SQLite
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }
else:
    import dj_database_url

    DATABASE_URL = get_env_variable("DATABASE_URL")
    DATABASES = {
        "default": dj_database_url.config(
            default=DATABASE_URL,
            conn_max_age=600,
            conn_health_checks=True,
        )
    }


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "America/New_York"

USE_I18N = True

# Removed per testing warning:  "RemovedInDjango50Warning: The USE_L10N setting is deprecated.
# Starting with Django 5.0, localized formatting of data will always be enabled.
# For example Django will display numbers and dates using the format of the current locale."
# USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

# URL where Django stages static files when site is running, so that browsers can request
# them via HTTP when building a page that contains static files.
STATIC_URL = "/static/"

# Tells Django where to check for static files other than apps.
# Used in development for serving static files.
# Used by 'collectstatic' command when compiling static files.
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# Tells Django where to store static files collected using 'manage.py collectstatic' command
# Location of static files during production.
STATIC_ROOT = BASE_DIR / "staticfiles"

# Specifies the 'file collection engine' used by collectstatic.
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Tells Django to use custom user model we defined in 'accounts' app
AUTH_USER_MODEL = "accounts.CustomUser"

# Tells where to redirect upon login and logout
LOGIN_REDIRECT_URL = "main:home"
LOGOUT_REDIRECT_URL = "main:home"

# Email - Uncomment/refactor as necessary to support email needs.
DEFAULT_FROM_EMAIL = get_env_variable("DEFAULT_FROM_EMAIL")
if ENV == "TEST":
    EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"
elif ENV == "DEV":
    # To Mail to Console
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
    # To Use SMTP
    # EMAIL_BACKEND = get_env_variable('EMAIL_BACKEND')
    # EMAIL_HOST = get_env_variable('EMAIL_HOST')
    # EMAIL_HOST_USER = get_env_variable('EMAIL_HOST_USER')
    # EMAIL_HOST_PASSWORD = get_env_variable('EMAIL_HOST_PASSWORD')
    # EMAIL_PORT = string_int_to_int(get_env_variable('EMAIL_PORT'))
    # EMAIL_USE_TLS = bool(int(get_env_variable('EMAIL_USE_TLS')))
else:
    # To Mail to Console
    # EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    # To Use SMTP
    EMAIL_BACKEND = get_env_variable("EMAIL_BACKEND")
    EMAIL_HOST = get_env_variable("EMAIL_HOST")
    EMAIL_HOST_USER = get_env_variable("EMAIL_HOST_USER")
    EMAIL_HOST_PASSWORD = get_env_variable("EMAIL_HOST_PASSWORD")
    EMAIL_PORT = string_int_to_int(get_env_variable("EMAIL_PORT"))
    EMAIL_USE_TLS = bool(int(get_env_variable("EMAIL_USE_TLS")))

# #For security
SECURE_SSL_REDIRECT = bool(int(get_env_variable("SECURE_SSL_REDIRECT")))
SECURE_PROXY_SSL_HEADER = (
    "HTTP_X_FORWARDED_PROTO",
    "https",
)  # Added for Heroku deploy with Docker
SECURE_HSTS_SECONDS = int(get_env_variable("SECURE_HSTS_SECONDS"))
SECURE_HSTS_INCLUDE_SUBDOMAINS = bool(
    int(get_env_variable("SECURE_HSTS_INCLUDE_SUBDOMAINS"))
)
SECURE_HSTS_PRELOAD = bool(int(get_env_variable("SECURE_HSTS_PRELOAD")))
SESSION_COOKIE_SECURE = bool(int(get_env_variable("SESSION_COOKIE_SECURE")))
CSRF_COOKIE_SECURE = bool(int(get_env_variable("CSRF_COOKIE_SECURE")))

if DEBUG:
    # For Django Debug Toolbar
    INSTALLED_APPS += [
        "django_extensions",
        "debug_toolbar",
    ]
    MIDDLEWARE += [
        "debug_toolbar.middleware.DebugToolbarMiddleware",
    ]


## comment for test commit
