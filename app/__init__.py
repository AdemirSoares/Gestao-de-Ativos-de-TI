from flask import Flask

from flask_migrate import Migrate

from app.config import Config
from app.database import db
from app.routes import init_app
from app import models

migrate = Migrate()


def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)

    migrate.init_app(app, db)

    init_app(app)

    return app