#!/usr/bin/env bash
git pull
docker-compose build
docker-compose up -d
docker-compose run --rm uwsgi python manage.py migrate --noinput --settings project.settings_docker
docker-compose run --rm uwsgi python manage.py collectstatic --noinput --settings project.settings_docker
