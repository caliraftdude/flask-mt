from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate 
from config import Config
from flask_login import LoginManager


# Application and Appliction configuration
app = Flask(__name__)
app.config.from_object(Config)

# Database and Database migration management
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Login support and management
login = LoginManager(app)
login.login_view = 'login'

# Avoid circular inclusion
from app import routes, models

