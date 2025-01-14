# Use the official Python image (you can change the version according to your needs)
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy the requirements.txt file from source code (not development dependencies)
COPY src/requirements.txt .

# Install project dependencies
RUN pip install -r requirements.txt 