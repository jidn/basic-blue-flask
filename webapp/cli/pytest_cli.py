"""Run pytest from `flask` command-line

flask test
"""
import pathlib
import click
import pytest


@click.command(context_settings=dict(ignore_unknown_options=True))
@click.argument("pytest_args", nargs=-1, type=click.UNPROCESSED)
def test(pytest_args):
    """Run tests using pytest."""

    root_dir = pathlib.Path(__file__).absolute().parents[2]
    test_dir = root_dir / "tests"
    args = [str(test_dir)]
    args.extend(pytest_args)
    exit(pytest.main(args))
