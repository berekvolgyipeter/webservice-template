# Use the official Python image as a parent image
FROM python:3.11-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . ./

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 8080

# Define environment variables
# (To allow the Flask application container to connect to the PostgreSQL database container,
# we use the service name defined in docker-compose.yml instead of "localhost" as the database host.
# By default, Docker Compose sets up a network
# that allows containers to resolve each other's service names as hostnames.)
ENV DB_URL postgresql://dbuser:dbpass@postgres:5432/webservice-db
ENV HOST 0.0.0.0
ENV PORT 8080

# Command to run the application with Gunicorn
CMD ["gunicorn", "--bind", "${HOST}:${PORT}", "app.main:app"]
