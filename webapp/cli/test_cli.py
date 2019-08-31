"""Add test to Flask command line
"""
import click


@click.command()
def test():
    """Run application tests."""
    from webapp.app import create_app

    client = create_app().test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert response.data == b"Hello World!"
    print("Passed tests")
