# Use the official PostgreSQL image from Docker Hub
FROM postgres:latest

# Set environment variables
ENV POSTGRES_DB=webservice-db
ENV POSTGRES_USER=dbuser
ENV POSTGRES_PASSWORD=dbpass

# Expose PostgreSQL default port
EXPOSE 5432
