import json
import os
import logging
from flask import Flask
from .configuration import configure
from .extensions import db, migrate
from .routes import main
from datetime import timedelta
from dotenv import load_dotenv
from flasgger import Swagger
from logging.handlers import RotatingFileHandler

load_dotenv()

def setup_logging(app):
    """Set up logging configuration."""
    # Set the log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    app.logger.setLevel(logging.DEBUG)

    # Create a file handler to store logs
    file_handler = RotatingFileHandler('error.log', maxBytes=100000, backupCount=3)
    file_handler.setLevel(logging.ERROR)

    # Create a console handler for logging
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    # Create a log format
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    # Attach formatter to handlers
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add handlers to the app's logger
    app.logger.addHandler(file_handler)
    app.logger.addHandler(console_handler)

def create_app():
    app = Flask(__name__)
    app.config.from_object(configure)
    
    # Set up logging
    setup_logging(app)

    db.init_app(app)
    app.register_blueprint(main)
    migrate.init_app(app, db)
    with open("swagger.json") as spec_file:
        swagger_config = json.load(spec_file)
    Swagger(app,template=swagger_config)
    with app.app_context():
        pass
    
    app.secret_key = os.getenv('FLASK_SECRET_KEY', 'SECRET_KEY')
    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)

    return app
