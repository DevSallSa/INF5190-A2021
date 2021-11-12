import os
from datetime import timedelta

class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = "mysecret"

    SESSION_COOKIE_SECURE = True

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    SESSION_COOKIE_SECURE = False
    SESSION_COOKIE_NAME = "google-login-session"

    PERMANENT_SESSION_LIFETIME = timedelta(minutes=1)

class TestingConfig(Config):
    TESTING = True
