#!/bin/bash

python3 -mvenv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py makemigrations spider
python3 manage.py migrate
python3 manage.py runserver