#!/bin/sh

python3 manage.py migrate

python3 manage.py makemigrations

python3 manage.py migrate

python3 add_admin.py

gunicorn -w4 -b 0.0.0.0:8000 rememberActivity.wsgi
