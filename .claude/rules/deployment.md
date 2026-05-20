---
paths:
  - "Dockerfile"
  - "docker-compose.yaml"
  - "k8s-deployment/**.yaml"
---

# Deployment

App and Postgres ship as separate container workloads, wired together by environment variables that ultimately resolve into `app.constants`. Two parallel topologies exist: local `docker-compose` and Kubernetes manifests under `k8s-deployment/`. Make targets (`make build-*`, `make up`, `make deploy-*`) are the canonical entrypoints.

## Design intent

- App and Postgres are independent workloads in both topologies and reach each other by service name (`postgres`). The host-process workflow is the only context that uses `localhost`.
- The Postgres image is built from `app/database/Dockerfile`, not pulled stock — so any DB-side init can be baked in. `make build-db` and the compose `postgres` service both target it.
- The env contract is the integration boundary. Every required var in `app/constants.py` must be supplied by compose (`env_file` + `environment`) or by k8s (`ConfigMap` for non-secrets, `Secret` for credentials).

## Patterns

- Local: `.env` → compose `env_file` → container env → `app.constants`. Compose overrides host-only vars (`POSTGRES_HOST=postgres`) in the `environment` block.
- K8s: `*-config.yaml` (non-secret) + `postgres-secret.yaml` (credentials) → Deployment `env.valueFrom` refs → container env.
- App entrypoint is `gunicorn ... app.main:app` bound to `APP_HOST:APP_PORT`; both come from env, not hard-coded in the Dockerfile CMD.

## Conventions

- One Deployment + Service pair per workload, in its own YAML file under `k8s-deployment/`.
- Image references in `k8s-deployment/*.yaml` use a hard-coded Docker Hub namespace from the template author — override before deploying anywhere real.

## Gotchas

- `.env` ships `POSTGRES_HOST=localhost` for host-process runs; the compose `POSTGRES_HOST=postgres` override is what makes the containerised app reach the DB. Don't move that into `.env`.
- `make deploy-postgres` applies `postgres-secret.yaml` instead of `postgres.yaml` — known template mismatch; apply `k8s-deployment/postgres.yaml` directly when bringing up the DB workload.
