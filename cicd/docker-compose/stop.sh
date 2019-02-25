#!/usr/bin/env bash
docker-compose stop nginx
docker-compose kill -s SIGINT uwsgi
docker-compose stop db redis
