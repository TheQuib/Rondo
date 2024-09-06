# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set environment variables to prevent Python from buffering output
ENV PYTHONUNBUFFERED=1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    python3-dev \
    libatlas-base-dev \
    build-essential \
    libffi-dev \
    gcc \
    pigpio \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy the entire src directory into the container
COPY src/ /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Default command to run the application
CMD ["sh", "-c", "pigpiod && python main.py"]
#CMD ["python", "main.py"]
