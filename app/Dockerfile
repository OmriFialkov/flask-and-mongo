# Use the official Python image as a base
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the app files into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install Ping
RUN apt-get update && apt-get install -y iputils-ping
RUN apt-get install -y nano

# Expose the port Flask will run on
EXPOSE 5000

# Set the command to run the Flask app
CMD ["python", "app.py"]
