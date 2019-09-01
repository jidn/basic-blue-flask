"""Hello world example blueprint.
"""
from flask import Blueprint

BLUEPRINT = Blueprint("main", __name__)


@BLUEPRINT.route("/")
def hello_world():
    """Say hello"""
    return "Hello World!"
