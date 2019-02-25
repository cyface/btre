#!/usr/bin/env bash
docker-compose run uwsgi python manage.py migrate --noinput
docker-compose run uwsgi python manage.py loaddata realtors
docker-compose run uwsgi python manage.py loaddata listings
docker-compose run uwsgi python manage.py createsuperuser
