#!/bin/bash

cd /home/ec2-user/flask-rds-project

git pull origin main

source venv/bin/activate

pip install -r requirements.txt

sudo systemctl restart nginx

