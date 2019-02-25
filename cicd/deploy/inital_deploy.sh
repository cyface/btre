#!/usr/bin/env bash
. .venv/bin/activate
python manage.py migrate
python manage.py loaddata initial_data
