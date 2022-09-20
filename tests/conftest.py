import pytest
from surfersapi import create_app
from surfersapi.data.models import db

@pytest.fixture(scope="session")
def app():
    app = create_app('testing')
    return app


@pytest.fixture(scope='module')
def new_feed(app):
    with app.app_context():
        from surfersapi.data.models import Feed
        _feed = Feed(name='BOM',
                    location='sydney',
                    category='weather',
                    url='http://weather')
        return _feed


@pytest.fixture(scope='module')
def test_client(app):

    # Create a test client using the Flask application configured for testing
    with app.test_client() as testing_client:
        # Establish an application context
        with app.app_context():
            yield testing_client  # this is where the testing happens
