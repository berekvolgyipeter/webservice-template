import pytest
from flask.testing import FlaskClient
from typing import Iterator

from app.main import app


@pytest.fixture
def mock_client() -> Iterator[FlaskClient]:
    """Fixture for using test app."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client
