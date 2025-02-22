#!/bin/sh
python3 -m venv env
source ./env/bin/activate && pip install --upgrade pip && pip install -r requirements.txt && python3 manage.py makemigrations && python3 manage.py migrate && python manage.py createsuperuser
