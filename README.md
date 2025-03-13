# webservice-template

This project implements a REST API webservice using PostgreSQL and Flask.
It is running in 2 containers: one for the application and one for the database.
The application is configured to run on a local machine, using `.env` file to store the secrets.
While this is not the safest way to store credentials, this project is for demonstration only.
In production, please make sure to store your secrets in encrypted format in a safe place.

## Dependencies

- [Docker](https://docs.docker.com/get-started/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Python 3.11](https://www.python.org/downloads/release/python-31111/)

## How to use

1. Create a `.env` file and specify all the environment variables listed in `.env.example`
2. Install requirements
   - `pip3 install -r requirements.txt`
2. Create the containers
    - `docker-compose up`
3. Since this is the first time the database is created, we need to apply migrations:
    - `alembic upgrade head`
    - more about migrations in `alembic/README.md`
4. We have a webservice running at `localhost:8080`

## Testing

For the testing we use a different database.
Before running the tests, we must create the test database:

`docker-compose -f docker-compose-test.yaml up`

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
