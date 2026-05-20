---
paths:
  - "app/database/**"
---

# Database

SQLAlchemy ORM layer: one shared declarative `Base`, a module-private engine and sessionmaker, ORM models with `to_dict()`, and a `utils.py` of query/mutation helpers consumed by interactors.

## Design intent

- `Base`, `__engine`, `__Session` live in `app/database/__init__.py` and are created at import time. Never construct a second engine or sessionmaker — Alembic and tests both rely on this single `Base.metadata`.
- Models declare relationships with `back_populates` on both sides and expose `to_dict()` for response serialisation. Keep `to_dict()` outputs flat — relationships are loaded on demand by callers that need them.
- `db_utils` is the only place that calls `get_session()`. Routes and interactors never touch sessions directly.

## Patterns

- New session per call: `session = get_session()` at the top of each util function. No request-scoped sessions, no context managers — the template trades pool efficiency for simplicity.
- Filtered list query:
  ```python
  query = session.query(Model)
  for key, value in vars(model_in).items():
      if value:
          query = query.filter_by(**{key: value})
  return query.all()
  ```
- Mutations call `session.add(...)` then `session.commit()`. Raise domain exceptions (e.g. `DriverNotFound`) before mutating when a referenced row is missing.

## Conventions

- Constraints (`UniqueConstraint`, `CheckConstraint`) go in `__table_args__` with named constraint strings so Alembic autogenerate produces stable names.
- Every model has `created_at` and `last_update` columns wired to `datetime.now` (`default=` / `onupdate=`).

## Gotchas

- Sessions opened in utils are never explicitly closed. That's fine for the template's load profile but don't reuse the pattern for long-running batch jobs.
- Alembic's `env.py` does `from app.database.models import Base` and uses `Base.metadata` as `target_metadata`. That import transitively registers every model class on `Base.metadata`. Narrowing it (e.g. importing `Base` from `app.database` directly, bypassing `models`) would silently break autogenerate — new tables wouldn't be detected.
