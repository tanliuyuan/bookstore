import logging
import os

from flask import Flask
from . import commands
from .models import db
from .views.v1 import book, user, role


logger = logging.getLogger(__name__)


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
        'SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Make trailing slashes optional for all routes
    app.url_map.strict_slashes = False
    
    db.init_app(app)

    # Register CLI commands
    app.register_blueprint(commands.bp)
    
    # Register API routes
    app.register_blueprint(book.bp)
    app.register_blueprint(user.bp)
    app.register_blueprint(role.bp)

    return app
