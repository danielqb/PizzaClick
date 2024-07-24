# Dockerfile

# Use an official Python base image
FROM python:3.9-slim AS pizzaclick

# Set the working directory in the container
WORKDIR /app

# Copy the project contents to the working directory
COPY apps/pizzaclick .

# Copy the requirements files and then install them
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Expose the port that the application will use
EXPOSE 8000

# Command to run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]