"""Flask app factory function."""
from flask import Flask
from webapp.cli import register_commands
from webapp.blueprints import register_blueprints


def create_app():
    """An application factory.
    """
    app = Flask(__name__, static_folder=None)

    # Hook everything up
    register_commands(app)
    register_blueprints(app)
    return app
