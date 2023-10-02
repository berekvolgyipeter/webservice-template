import os


IS_DEV_ENVIRONMENT = True
DB_URL = os.getenv("DB_URL", "postgresql://dbuser:dbpass@localhost:5432/webservice-db")
HOST = os.getenv("HOST", "0.0.0.0")
PORT = int(os.getenv("PORT", 8080))
DEFAULT_RATE_LIMIT = "4/minute"

STATUS_OK = {"status": "OK"}
