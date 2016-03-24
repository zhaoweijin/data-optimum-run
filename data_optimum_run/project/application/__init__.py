# coding: utf-8
import sys
import os

# Insert project root path to sys.path
project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_path not in sys.path:
    sys.path.insert(0, project_path)

import time
from flask import Flask
from config import load_config

# convert python's encoding to utf8
try:
    from imp import reload

    reload(sys)
    sys.setdefaultencoding('utf8')
except (AttributeError, NameError):
    pass


def create_app():
    """Create Flask app."""
    config = load_config()

    app = Flask(__name__)
    app.config.from_object(config)

    # Register components
    register_db(app)
    return app

def register_db(app):
    """Register models."""
    from .models import db

    db.init_app(app)

