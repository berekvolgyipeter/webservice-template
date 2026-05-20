# webservice-template

A small REST API template built on Flask, SQLAlchemy and PostgreSQL, packaged with Docker. The schema models a Formula 1 domain (drivers and their grand prix results) for demonstration.

The app and database run in separate containers. Configuration is loaded from a local `.env` file — adequate for a demo, but production deployments should source secrets from a managed store.

## Stack

- Flask, Flask-Limiter, Gunicorn
- PostgreSQL, SQLAlchemy, Alembic (migrations)
- `schema` for request validation
- pytest for tests
- Docker, Docker Compose

## Layout

```
app/
  routes/        Flask blueprints (HTTP layer)
  schemas/       request validation and input DTOs
  interactors/   orchestration between routes and the database
  database/      SQLAlchemy models and query helpers
alembic/         migrations
tests/           pytest suite, mirrors app/
```

## Dependencies

- [Docker](https://docs.docker.com/get-started/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Python 3.11](https://www.python.org/downloads/release/python-31111/)

## Getting started

1. Copy `.env.example` to `.env` and fill in the variables.
2. Install Python dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Build and start the containers:
   ```sh
   docker-compose up
   ```
4. Apply migrations (only required on a fresh database):
   ```sh
   alembic upgrade head
   ```
   See [`alembic/README.md`](alembic/README.md) for the migration workflow.
5. The service is reachable at `http://localhost:8080`.

## Endpoints

| Method | Path       | Purpose                      |
|--------|------------|------------------------------|
| GET    | `/`        | Health check                 |
| GET    | `/drivers` | List drivers (filterable)    |
| POST   | `/drivers` | Create a driver              |
| GET    | `/results` | List grand prix results      |
| POST   | `/results` | Record a result for a driver |

## Testing

Tests run against a dedicated database container:

```sh
pip install -r requirements_test.txt
docker-compose -f docker-compose-test.yaml up -d
pytest
```

Alembic migrations are applied automatically by a session-scoped pytest fixture, so no manual setup is required between runs.

## Kubernetes deployment

Manifests live in `k8s-deployment/` and target a local single-node cluster (minikube). The corresponding Make targets are shown in parentheses.

1. Start the cluster (`make minikube-start`).
2. Apply the Postgres ConfigMap and Secret (`make deploy-postgres-config`, `make deploy-postgres-secret`).
3. Deploy Postgres (`make deploy-postgres`).
4. Apply the app ConfigMap and deploy the app (`make deploy-app-config`, `make deploy-app`).
5. Resolve the app's URL (`make minikube-app-url`).

The topology is intentionally minimal: a single-replica app Deployment and a single-replica Postgres Deployment (not a StatefulSet) backed by its own PersistentVolume inside the cluster. Suitable for local exercises, not for production.
