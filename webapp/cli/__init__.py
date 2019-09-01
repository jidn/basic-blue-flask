"""Add additional `flask` command-line options.
"""
from .lint_cli import lint
from .pytest_cli import test


def register_commands(app):
    """Register `Click` commands with flask app."""
    for command in (test, lint):
        app.cli.add_command(command)
