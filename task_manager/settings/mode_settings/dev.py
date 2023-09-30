from task_manager.settings.base import *

# ALLOWED_HOSTS = ['*']

# INTERNAL_IPS = [
#     '127.0.0.1',
# ]

# INSTALLED_APPS += [
#     'debug_toolbar',
#     # 'silk',
# ]
# MIDDLEWARE = [
#                  'debug_toolbar.middleware.DebugToolbarMiddleware',
#                  # 'silk.middleware.SilkyMiddleware',
#              ] + MIDDLEWARE

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')