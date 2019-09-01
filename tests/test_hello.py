"""Test hello world
"""


def test():
    """Run application tests."""
    from webapp.app import create_app

    client = create_app().test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert response.data == b"Hello World!"
