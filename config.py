import os
import random
import string

from decouple import config


BASE_DIR = os.path.abspath('.')
DEBUG = config('DEBUG', cast=bool)
SECRET_KEY = config('SECRET_KEY') or ''.join(random.choice(string.ascii_letters) for i in range(42))
SQLALCHEMY_DATABASE_URI = config('SQLALCHEMY_DATABASE_URI') or 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite')
SQLALCHEMY_TRACK_MODIFICATIONS = config('SQLALCHEMY_TRACK_MODIFICATIONS', True, cast=bool)

MAIL_SERVER = config('MAIL_SERVER')
MAIL_PORT = config('MAIL_PORT', cast=int)
MAIL_USERNAME = config('MAIL_USERNAME')
MAIL_PASSWORD = config('MAIL_PASSWORD')
MAIL_USE_TLS = config('MAIL_USE_TLS', cast=bool)
MAIL_USE_SSL = config('MAIL_USE_SSL', cast=bool)
MAIL_DEFAULT_SENDER = config('MAIL_DEFAULT_SENDER')