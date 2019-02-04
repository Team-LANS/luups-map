import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    DB_USER = os.getenv('DB_USER')
    DB_PW = os.getenv('DB_PW')
    DB_NAME = os.getenv('DB_NAME')
    SQLALCHEMY_DATABASE_URI = 'postgresql://{user}:{pw}@{address}/{db}'.format(
        user=DB_USER,
        pw=DB_PW,
        address='localhost:5432',
        db=DB_NAME
    )
    SECRET_KEY = os.getenv('SECRET_KEY')


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
