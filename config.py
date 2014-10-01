import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'

    # MySQL database connection info
    MYSQL_DATABASE_HOST = 'localhost'
    MYSQL_DATABASE_PORT = 3306
    MYSQL_DATABASE_USER = None
    MYSQL_DATABASE_PASSWORD = None
    MYSQL_DATABASE_DB = None
    MYSQL_DATABASE_CHARSET = 'utf8'

    # Brewerydb API info
    # For more information, see: http://www.brewerydb.com/developers/docs
    BREWERYDB_API_URL = 'http://api.brewerydb.com/v2'
    BREWERYDB_API_KEY = os.environ.get('BREWERY_DB_API_KEY')

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
