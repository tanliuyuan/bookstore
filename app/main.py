import logging
import os

from flask import Flask
from . import commands
from .models import db
from .views.v1 import book


logger = logging.getLogger(__name__)


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
        'SQLALCHEMY_DATABASE_URI')
    db.init_app(app)

    app.register_blueprint(commands.bp)
    app.register_blueprint(book.bp)

    return app
