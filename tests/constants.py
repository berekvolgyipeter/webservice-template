import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ALEMBIC_INI_ABS_PATH = os.path.join(BASE_DIR, "alembic.ini")
ALEMBIC_ABS_PATH = os.path.join(BASE_DIR, "alembic")

TEST_STATUS_OK = {"status": "OK"}
TEST_ROUTE_PARAMS = {"param": "value"}
