"""Access linting through `flask` command-line

flask lint              pylint
"""
from subprocess import call

import click


@click.command()
def lint():
    """Lint with Pylint."""

    command_line = ("pylint", "wsgi.py", "webapp")
    click.echo("Checking code: {}".format(" ".join(command_line)))
    returned = call(command_line)
    if returned != 0:
        exit(returned)
