# project/__init__.py
from flask import Flask
from project.service.sentiment_engine import SentimentEngine

def create_app(config_filename=None):
    print
    'Creating application with filename %s' % config_filename
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile(config_filename)
    initialize_extensions(app)
    return app


def initialize_extensions(app):
    app.engine = SentimentEngine()