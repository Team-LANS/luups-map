import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    CSRF_ENABLED = True
    SECRET_KEY = os.getenv('SECRET_KEY')

    # DB
    DB_USER = os.getenv('DB_USER')
    DB_PW = os.getenv('DB_PW')
    DB_NAME = os.getenv('DB_NAME')
    SQLALCHEMY_DATABASE_URI = 'postgresql://{user}:{pw}@{address}/{db}'.format(
        user=DB_USER,
        pw=DB_PW,
        address='localhost:5432',
        db=DB_NAME
    )


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    TESTING = False


class TestingConfig(Config):
    DEBUG = False
    TESTING = True


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
