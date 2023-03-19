import logging
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
db = SQLAlchemy(app)
logger = logging.getLogger(__name__)

with app.app_context():
    from models import book, log, role, user, user_role
    db.create_all()
