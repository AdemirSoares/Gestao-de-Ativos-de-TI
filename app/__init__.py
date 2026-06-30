from flask import Flask

from app.config import Config
from app.database import db
from app.routes import init_app


def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)

    init_app(app)

    return app