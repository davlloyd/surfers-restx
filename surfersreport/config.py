import os
from os import path
import sys

basedir = os.getcwd()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret'
    SESSION_COOKIE_HTTPONLY = False
    ENV = 'unset'

    @staticmethod
    def init_app(app):
        pass


class ProductionConfig(Config):
    ENV = 'production'

class DevelopmentConfig(Config):
    DEBUG = True
    ENV = 'development'

class TestingConfig(Config):
    TESTING = True
    ENV = 'testing'


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
