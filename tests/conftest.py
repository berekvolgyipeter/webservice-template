import pytest
from alembic import command
from alembic.config import Config
from flask.testing import FlaskClient
from typing import Iterator

from tests.constants import ALEMBIC_INI_ABS_PATH, ALEMBIC_ABS_PATH

from app.database import get_session, Base
from app.main import app


@pytest.fixture(scope="session", autouse=True)
def apply_migrations():
    """Run Alembic migrations before running tests."""
    alembic_cfg = Config(ALEMBIC_INI_ABS_PATH)
    alembic_cfg.set_main_option("script_location", ALEMBIC_ABS_PATH)
    command.upgrade(alembic_cfg, "head")
    yield


@pytest.fixture
def mock_session():
    """Provide a fresh test database session for each test."""
    session = get_session()

    Base.metadata.drop_all(bind=session.bind)
    Base.metadata.create_all(bind=session.bind)

    yield session

    session.rollback()
    session.close()


@pytest.fixture
def mock_client() -> Iterator[FlaskClient]:
    """Fixture for using test app."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client
