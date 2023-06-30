import logging
import os
import commands
from flask import Flask
from models import db


logger = logging.getLogger(__name__)


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
        'SQLALCHEMY_DATABASE_URI')
    db.init_app(app)

    app.register_blueprint(commands.bp)

    return app
