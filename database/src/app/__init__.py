import os
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate

from src.app.config import app_config


database = SQLAlchemy()
ma = Marshmallow()


def create_app():
    app = Flask(__name__)
    app.config.from_object(app_config[os.getenv('FLASK_ENV')])
    database.init_app(app)
    ma.init_app(app)
    CORS(app)
    Migrate(app=app, db=database, directory="./src/app/migrations")
    from src.app.models import ad, game
    return app
