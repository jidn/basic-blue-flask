from flask import Blueprint

blueprint = Blueprint("main", __name__)


@blueprint.route("/")
def HelloWorld():
    """Say hello"""
    return "Hello World!"
