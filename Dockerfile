# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set environment variables to prevent Python from buffering output
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /home/pi/rondo

# Copy the requirements file into the container
COPY src/requirements.txt /home/pi/rondo/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire src directory into the container
COPY src/ /home/pi/rondo/

# Default command to run the application
CMD ["python", "main.py"]
