-include .env

up :; docker-compose up --build
up-db :; docker-compose up postgres
up-app :; docker-compose up app
down :; docker-compose down
delete-db :; rm -rf postgres-data/
