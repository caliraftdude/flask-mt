import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or '6BC53AADC21E6B6EAA3A354A6326FB6EF57EC56A650944D541FE45153080A726127F2BB446B6A7F47AA2456C722BFF569D195A1F617F7935A60D4CAA38A953DD'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqllite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False # disables signalling the app everytime a change is going to be made to the db
    