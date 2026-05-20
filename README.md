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

This time we don't have to do any migrations, there's a pytest fixture which takes care about this.
Now the tests are ready to run.

## Kubernetes deployment

1. create a single-node k8s cluster with minikube
2. deploy postgres config
3. deploy postgres secrets
4. deploy postgres
5. deploy app config
6. deploy app
7. get the URL of the app

- all of these steps are listed in the `Makefile`
- the database uses a different volume inside the cluster
- this deployment is very simple
  - only 1 replica for the app deployment
  - postgres is also a 1 replica deployment instead of a stateful set
Alembic migrations are applied automatically by a session-scoped pytest fixture, so no manual setup is required between runs.
