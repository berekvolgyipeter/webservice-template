---
paths:
  - "app/main.py"
  - "app/global_objects.py"
  - "app/constants.py"
  - "app/exceptions.py"
---

# App Core

Top-level Flask wiring: process entrypoint, shared singletons, environment-derived config, and cross-cutting exception helpers. Everything below depends on this layer; this layer depends only on stdlib + Flask + dotenv.

## Design intent

- Flask `app` and `limiter` live in `global_objects.py` so any module can import them without circular dependencies — never re-instantiate either elsewhere.
- `main.py` is the only place blueprints get registered. New routes ship as a new blueprint imported and registered here.
- All config flows through `constants.py`. Read env vars there, not at the call site, so the env contract is discoverable in one file.
- `POSTGRES_URL` is composed from parts in `constants.py`; never reconstruct it elsewhere.

## Patterns

- Required env vars use `os.environ[...]` (fail fast at import); optional ones use `os.getenv(..., default)`.
- `STATUS_OK = {"status": "OK"}` is the success-envelope literal — interactors spread it into responses.
- `http_exception(code, message)` is the way to abort with a JSON error body; raise domain exceptions (e.g. `DriverNotFound`) for non-HTTP layers to translate.

## Conventions

- New domain exceptions go in `exceptions.py` as bare `Exception` subclasses, named for the missing/invalid entity.
- Constants are SCREAMING_SNAKE_CASE; no runtime mutation.

## Gotchas

- `load_dotenv()` runs on import of `constants.py`; importing it before `.env` exists will crash because `POSTGRES_DB`/`USER`/`PASSWORD` are required.
- `IS_DEV_ENVIRONMENT` is hard-coded `True` — debug mode is always on. Treat that as a known template limitation, not a bug to "fix" silently.
