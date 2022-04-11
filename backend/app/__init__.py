from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from blueprints import register_bps
from flask_migrate import Migrate

def create_app():
    app = Flask(__name__)
    if app.config['ENV'] == "production":
        app.config.from_object('app.config.ProductionConfig')
    elif app.config['ENV'] == "testing":
        app.config.from_object('app.config.TestingConfig')
    elif app.config['ENV'] == "development":
        app.config.from_object('app.config.DevelopmentConfig')
    else:
        raise Exception("Invalid environment specified")
    return app

# creating flask app
app = create_app()

# registering blueprints
register_bps(app)

# setting up sqlalchemy db
db = SQLAlchemy(app)

from .models import *

migrate = Migrate(app, db)
