from dotenv import dotenv_values

_ENV = dotenv_values()

DEBUG = True
URL_PREFIX = '/api/v1'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://mariadb:mariadb@{_ENV["DB_HOST"]}/btalert'