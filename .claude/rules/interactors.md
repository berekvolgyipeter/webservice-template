---
paths:
  - "app/interactors/**.py"
---

# Interactors

The use-case layer between HTTP routes and the database. Each interactor function takes a validated `*In` DTO, calls into `app.database.utils`, and returns a serialisable dict. This is where domain logic (if any) belongs — routes stay declarative and DB utils stay query-only.

## Design intent

- One interactor module per resource, mirroring `app/routes/` and `app/schemas/` names.
- Interactors return dicts, not ORM objects. Always merge `STATUS_OK` into the response and project models via `model.to_dict()`.
- Catch nothing here unless a domain exception needs translating to an HTTP response — let `DriverNotFound` and friends propagate so callers can decide.

## Patterns

- List response: `{**STATUS_OK, "<resource>": [m.to_dict() for m in db_utils.list_x(x_in)]}`.
- Mutation response: call the db util, return bare `STATUS_OK`.

## Conventions

- Import db utils as `from app.database import utils as db_utils` so the call site reads `db_utils.<verb>_<resource>`.
- Function names match the route handler they back (`list_drivers`, `add_driver`, …).

## Gotchas

- Interactors are unit-tested against a live test DB via the `mock_session` fixture — keep them free of Flask imports so tests stay fast.
