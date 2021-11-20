import os
from datetime import timedelta

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = "mysecret"

    SESSION_COOKIE_SECURE = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:////' + os.path.join(BASE_DIR, 'database/database.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = True

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    SESSION_COOKIE_SECURE = False
    SESSION_COOKIE_NAME = "google-login-session"

    PERMANENT_SESSION_LIFETIME = timedelta(minutes=1)

class TestingConfig(Config):
    TESTING = True
