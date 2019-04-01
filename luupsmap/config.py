import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    CSRF_ENABLED = True
    SECRET_KEY = os.getenv('SECRET_KEY')
    GMAPS_API_KEY = os.getenv('GMAPS_API_KEY')

    # DB
    DB_USER = os.getenv('DB_USER')
    DB_PW = os.getenv('DB_PW')
    DB_ADDRESS = os.getenv('DB_ADDRESS')
    DB_NAME = os.getenv('DB_NAME')
    SQLALCHEMY_DATABASE_URI = 'postgresql://{user}:{pw}@{address}/{db}'.format(
        user=DB_USER,
        pw=DB_PW,
        address=DB_ADDRESS,
        db=DB_NAME
    )

    # DEBUG,...
    DEBUG = False
    DEVELOPMENT = False
    TESTING = False


class DevelopmentConfig(Config):
    DEBUG = True
    DEVELOPMENT = True


class TestingConfig(Config):
    DB_NAME = 'luups_map_test'
    TESTING = True


class ProductionConfig(Config):
    DB_NAME = 'luups_map'
