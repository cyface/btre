#!/usr/bin/env bash
docker-compose run uwsgi python manage.py migrate --noinput --settings project.settings_docker
docker-compose run uwsgi python manage.py loaddata realtors --settings project.settings_docker
docker-compose run uwsgi python manage.py loaddata listings --settings project.settings_docker
docker-compose run uwsgi python manage.py createsuperuser --settings project.settings_docker
