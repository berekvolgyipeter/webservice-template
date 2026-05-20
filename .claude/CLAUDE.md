# Project Instructions

Flask + SQLAlchemy + Alembic + PostgreSQL webservice template, layered as `routes → schemas → interactors → database`.

## Rule Files — Progressive Disclosure

Rules in `.claude/rules/` contain curated architectural knowledge: design intent, patterns, constraints, and conventions.

**Before answering questions, researching, or modifying code in any area below:** read the relevant rule file(s) FIRST. They explain the "why" and "how" without needing to scan source files. Only dive into source code for details the rules don't cover.

| Rule file | Triggers on | Covers |
|---|---|---|
| `app-core.md` | `app/main.py`, `app/global_objects.py`, `app/constants.py`, `app/exceptions.py` | Flask app wiring, shared `app`/`limiter` singletons, env-derived config, and domain exception helpers |
| `routes.md` | `app/routes/**.py`, `app/utils/__init__.py` | HTTP layer: blueprints, `@get_params` request parsing, rate limiting, route→schema→interactor flow |
| `interactors.md` | `app/interactors/**.py` | Use-case layer: orchestrates schemas and DB utils, returns `STATUS_OK`-merged response dicts |
| `schemas.md` | `app/schemas/**.py` | Request validation with the `schema` library: `*In` DTOs and the `validate_optional_*` / `validate_all_*` pair |
| `database.md` | `app/database/**` | SQLAlchemy layer: shared `Base`, module-private engine/sessionmaker, models with `to_dict()`, query helpers |
| `alembic.md` | `alembic/**`, `alembic.ini` | Migration env wiring (uses app's `Base.metadata` and `POSTGRES_URL`) and autogenerate workflow |
| `tests.md` | `tests/**`, `pytest.ini`, `docker-compose-test.yaml` | Pytest patterns: session-scoped migration fixture, per-test `mock_session`, `mock_client`, layered patch targets |
