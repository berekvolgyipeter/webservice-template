-include .env

# build docker images
build-db :; docker build -t webservice-template-postgres -f app/database/Dockerfile app/database/
build-app :; docker build -t webservice-template-app .

# push images to registry
docker-login :; docker login
tag-db :; docker tag webservice-template-postgres:latest $(DOCKER_ACCOUNT)/webservice-template-postgres:latest
tag-app :; docker tag webservice-template-app:latest $(DOCKER_ACCOUNT)/webservice-template-app:latest
push-db-to-registry :; docker push $(DOCKER_ACCOUNT)/webservice-template-postgres:latest
push-app-to-registry :; docker push $(DOCKER_ACCOUNT)/webservice-template-app:latest

# compose
up :; docker-compose up -d
up-db :; docker-compose up postgres -d
up-app :; docker-compose up app -d
down :; docker-compose down
delete-db :; rm -rf postgres-data/

# compose test db
up-test-db :; docker-compose -f docker-compose-test.yaml up -d
down-test :; docker-compose -f docker-compose-test.yaml down
