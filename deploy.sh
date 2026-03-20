#!/bin/bash

cd /home/ec2-user/flask-rds-project

# Create venv if not exists
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi

# Activate venv
source venv/bin/activate

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Kill old gunicorn if running
pkill gunicorn || true

# Start app
nohup gunicorn -w 4 -b 0.0.0.0:8080 app:app > output.log 2>&1 &
