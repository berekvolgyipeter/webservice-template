-include .env

up :; docker-compose up -d
up-db :; docker-compose up postgres -d
up-app :; docker-compose up app -d
down :; docker-compose down
delete-db :; rm -rf postgres-data/

up-test-db :; docker-compose -f docker-compose-test.yaml up -d
down-test :; docker-compose -f docker-compose-test.yaml down
