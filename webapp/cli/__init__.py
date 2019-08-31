"""Add additional `flask` command-line options.
"""
from .test_cli import test


def register_commands(app):
    """Register `Click` commands with flask app."""
    app.cli.add_command(test)
