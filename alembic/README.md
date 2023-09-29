Generic single-database configuration.

if alembic has just been installed:<br>
`alembic init alembic`<br>
• make sure to connect model metadata in env.py<br>
• in alembic.ini, remove the setting of `sqlalchemy.url`<br>
• set it in env.py:<br>
`config.set_main_option('sqlalchemy.url', <your db url>)`

---
when DB is set up with docker compose, open a new terminal and set the DB_URL env var:<br>
`export DB_URL=postgresql://dbuser:dbpass@localhost:5432/webservice-db`

snyc db:<br>
`alembic upgrade head`

generate migration script:<br>
`alembic revision --autogenerate -m "your revision name"`

apply the migration:<br>
`alembic upgrade head`
---

to check revision history:<br>
`alembic history`

to downgrade to previous revision:<br>
`alembic downgrade -1`
