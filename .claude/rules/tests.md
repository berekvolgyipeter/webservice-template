---
paths:
  - "tests/**"
  - "pytest.ini"
  - "docker-compose-test.yaml"
---

# Tests

Pytest suite organised as `tests/unit/<layer>/test_<resource>*.py`, mirroring the `app/` tree. Each layer is tested at the appropriate seam: routes with mocked schemas/interactors, schemas via parametrised inputs, interactors against a real (test) database.

## Design intent

- The test DB is a separate Postgres container declared in `docker-compose-test.yaml`, exposed on port 7654. `pytest.ini` injects the matching env vars so `app.constants` resolves to it at import time.
- `apply_migrations` is `scope="session", autouse=True` and runs `alembic upgrade head` once — never apply migrations from inside a test.
- `mock_session` drops and recreates all tables per test for isolation. Use it for interactor / DB-util tests. Don't share state between tests.
- `mock_client` yields a Flask test client with `TESTING=True`. Use it for route tests.

## Patterns

- Route test (no DB): patch the resource module's `schema` and `interactor` aliases.
  ```python
  @patch("app.routes.<r>.schema.validate_all_<r>_in", return_value=TEST_ROUTE_PARAMS)
  @patch("app.routes.<r>.interactor.<verb>_<r>", return_value=TEST_STATUS_OK)
  def test_<verb>_<r>(mock_interactor, mock_schema, mock_client): ...
  ```
- Interactor test: take `mock_session`, call interactor functions directly, assert on the returned dict.
- Schema test: `@mark.parametrize("params, exp_is_valid", [...])`, try/except `SchemaError`.

## Conventions

- Shared fixtures live in `tests/conftest.py`. Shared literals (`TEST_STATUS_OK`, `TEST_ROUTE_PARAMS`, alembic paths) live in `tests/constants.py`.
- One test module per resource per layer. Naming varies by layer — match the existing convention in each directory:
  - `tests/unit/routes/test_<resource>.py` (no layer suffix)
  - `tests/unit/schemas/test_<resource>_schema.py` (singular `schema`)
  - `tests/unit/interactors/test_<resource>_interactors.py` (plural `interactors`)

## Gotchas

- Patch targets are the route module's `schema` / `interactor` aliases, not the original modules — e.g. `app.routes.drivers.schema.validate_all_drivers_in`, not `app.schemas.drivers.validate_all_drivers_in`. Patching the wrong path silently does nothing.
- Tests rely on the test DB being up before the session-scoped fixture runs. CI brings it up as a service in `.github/workflows/test.yml`; locally use `make up-test-db`.
