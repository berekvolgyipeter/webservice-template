# Use the official Python image as a parent image
FROM python:3.11-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . ./

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Command to run the application with Gunicorn
CMD sh -c "gunicorn --bind ${APP_HOST}:${APP_PORT} app.main:app"
