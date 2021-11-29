"""
This module contains different configurations for specific
tasks
"""

class BaseConfig(object):
    DEBUG = False
    TESTING = False

class DevConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    USE_RELOADER = False
    MONGODB_SETTINGS = {'db': 'testing'}
    SECRET_KEY = 'flask+mongoengine=<3'
    DEBUG_TB_INTERCEPT_REDIRECTS = True
    WTF_CSRF_ENABLED = False

class TestingConfig(BaseConfig):
    DEBUG = False
    TESTING = True
    SECRET_KEY = 'flask+mongoengine=<3'
    MONGODB_SETTINGS = {'db': 'testing'}
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    WTF_CSRF_ENABLED = False
