---
paths:
  - "app/routes/**.py"
  - "app/utils/__init__.py"
---

# HTTP Routes

Flask blueprints — the thin HTTP layer. Each resource gets its own blueprint module that parses the request, hands a dict to a schema validator, calls the matching interactor, and returns `(dict, status_code)`. No business logic lives here.

## Design intent

- One blueprint per resource, `url_prefix="/<resource>"`, registered in `app/main.py`.
- Routes stay declarative: extract params → validate → delegate → return. If a handler needs branching logic, it belongs in the interactor.
- Request parsing is centralised in the `@get_params` decorator so handlers receive a `params: dict` regardless of method. Don't touch `flask.request` directly inside handlers.

## Patterns

- Standard handler shape:
  ```python
  @api.get("")
  @limiter.limit(DEFAULT_RATE_LIMIT)
  @get_params
  def list_x(params: dict) -> tuple[dict, int]:
      x_in = schema.validate_optional_x_in(params)
      return interactor.list_x(x_in), 200
  ```
- Import schemas and interactors as `schema` / `interactor` aliases so tests can patch `app.routes.<resource>.schema.<fn>` and `app.routes.<resource>.interactor.<fn>`.
- `@get_params` returns `request.json` for POST/PUT/PATCH and `dict(request.args)` for everything else.

## Conventions

- Apply `@limiter.limit(DEFAULT_RATE_LIMIT)` to read endpoints (GETs). Write endpoints are currently unlimited — match that unless the user asks otherwise.
- Return tuples, never `flask.jsonify(...)` — Flask serialises dicts automatically and tests assert on `response.json`.

## Gotchas

- The decorator stack order matters: `@api.<verb>` outermost, then `@limiter.limit`, then `@get_params` innermost. Reordering changes how Flask sees the view function.
- `health` blueprint uses `url_prefix="/"`, so its route registers at the app root; other blueprints prefix with the resource name.
