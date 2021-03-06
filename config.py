import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # Database
    SECRET_KEY = os.environ.get('SECRET_KEY') or '6BC53AADC21E6B6EAA3A354A6326FB6EF57EC56A650944D541FE45153080A726127F2BB446B6A7F47AA2456C722BFF569D195A1F617F7935A60D4CAA38A953DD'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False # disables signalling the app everytime a change is going to be made to the db

    # Mail support
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['admin@example.com']

    # Application behavior
    POSTS_PER_PAGE = 20

    # Babel language support
    LANGUAGES = ['en', 'es']

    # Translator Services
    MS_TRANSLATOR_KEY = os.environ.get('MS_TRANSLATOR_KEY')
    