#!/bin/sh

echo 'Waiting PostgreSQL'

while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
    sleep 0.5
done

echo 'PostgreSQL started'

poetry run python3 manage.py migrate

exec "$@"