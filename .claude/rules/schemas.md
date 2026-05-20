---
paths:
  - "app/schemas/**.py"
---

# Schemas

Request-shape validation built on the `schema` library. Each module defines a plain `*In` DTO class plus two validators: one that requires every field (for create/replace) and one that allows any subset (for filtered list).

## Design intent

- DTOs are plain classes with typed `__init__` defaults, not dataclasses or Pydantic models — keep the dependency surface small and let `vars(dto)` round-trip cleanly into `**kwargs` for both DB queries and ORM construction.
- Validation lives here and only here. Routes call `validate_*`; interactors and db utils trust their `*In` argument.
- The optional/all split exists because list endpoints accept any subset of filters while create endpoints demand the full object.

## Patterns

- Per resource, export:
  - `class <Resource>In` with one kwarg per field, defaulting to `None`.
  - `OPTIONAL_<RESOURCE>_IN = Schema({Optional("field"): T, ...}, ignore_extra_keys=True)`.
  - `ALL_<RESOURCE>_IN = Schema({"field": T, ...}, ignore_extra_keys=True)`.
  - `validate_optional_<resource>_in(params)` — runs the optional schema, then raises `SchemaError` if no field was supplied, then returns `<Resource>In(**params)`.
  - `validate_all_<resource>_in(params)` — runs the all-schema and returns `<Resource>In(**params)`.
- Use `And(Use(int), lambda x: x > 0)` for coerced + bounded numeric fields (see `results.position`).

## Conventions

- Schemas pass `ignore_extra_keys=True` so unknown query-string params don't 400. Don't tighten this without checking callers.
- Raise `SchemaError` (already imported from `schema`) for cross-field rules — don't invent a custom exception type.

## Gotchas

- `vars(<Resource>In())` returns every field including `None`s. `db_utils` relies on this to skip empty filters via `if value:` — preserve that contract when adding new fields (no truthy defaults like `0` or `""`).
