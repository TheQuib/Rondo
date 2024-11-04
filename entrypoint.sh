#!/bin/bash

# Function to clean up GPIO on exit
cleanup() {
    python -c "import RPi.GPIO as GPIO; GPIO.setmode(GPIO.BCM); GPIO.setup(23, GPIO.OUT); GPIO.output(23, GPIO.LOW); GPIO.cleanup()"
    echo "LED turned off on container exit."
}

# Trap the EXIT signal to run the cleanup function
trap cleanup EXIT

# Run the main application
python main.py