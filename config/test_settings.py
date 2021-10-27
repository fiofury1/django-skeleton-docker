from .settings import *

DEBUG = False

DATABASES = {
    "default": {
    "ENGINE": "django.db.backends.sqlite3",
    "NAME": ":memory:",                   #OR 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'