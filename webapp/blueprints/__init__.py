"""Import all `flask.Blueprint` modules.

Just drop the blueprint modules in the same directory. The only requirement is
the a `Flask.Blueprint` object named 'BLUEPRINT' in the __init__.py

EXAMPLE

    from flask import Blueprint
    BLUEPRINT = Blueprint("myBlueprint", __name__)

    @BLUEPRINT.route("/")
    def hello_world():
        return "Hello World!"
"""
from . import main


def register_blueprints(app):
    """Register blueprints on application."""
    app.register_blueprint(main.BLUEPRINT)
