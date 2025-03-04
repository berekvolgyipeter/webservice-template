# Generic single-database configuration.  
  
## At first usage  
  
- if alembic has just been installed:  
    - `alembic init alembic`  
- make sure to connect model metadata in env.py  
- in alembic.ini, remove the setting of `sqlalchemy.url`  
- set it in env.py:  
  - `config.set_main_option('sqlalchemy.url', <your db url>)`  
  
## After DB container has been created with docker-compose  
  
- open a new terminal and set the env vars:  
  - `source .env`  
  
- snyc db:  
  - `alembic upgrade head`  
  
- generate migration script:  
  - `alembic revision --autogenerate -m "your revision name"`  
  
- apply the migration:  
  - `alembic upgrade head`  
  
to check revision history:<br>  
`alembic history`  
  
to downgrade to previous revision:<br>  
`alembic downgrade -1`
