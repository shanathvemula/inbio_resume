from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-7t(7ld7#i2hy!(nb1x!utfhvkm3#_$_dsohl9re=wxxi=pnz^e"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

# Email Settings
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp-mail.outlook.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = 'shanathvemula@outlook.com'
EMAIL_HOST_PASSWORD = 'Vemula_1606'
EMAIL_USE_TLS = True

try:
    from .local import *
except ImportError:
    pass
