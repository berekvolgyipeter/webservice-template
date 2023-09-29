Generic single-database configuration.

if alembic has just been installed:<br>
`alembic init alembic`<br>
• make sure to connect model metadata in env.py<br>
• in alembic.ini, set `sqlalchemy.url = ${DB_URL}`

when DB is set up with docker compose, open a new terminal and set the DB_URL env var:<br>
`export DB_URL=postgresql://dbuser:dbpass@localhost:5432/webservice-db`

generate migration script:<br>
`alembic revision --autogenerate -m "your revision name"`

apply the migration:<br>
`alembic upgrade head`

