from dotenv import dotenv_values

_ENV = dotenv_values()

DEBUG = True
URL_PREFIX = '/api/v1'
SQLALCHEMY_TRACK_MODIFICATIONS = False

DB_USER = 'app_btalert'
DB_PASSWORD = 'k%21w%5E%3DAn%29KQtJwZ%3AWa%22n%40_%3D8S'
SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{_ENV["DB_HOST"]}/btalert'
