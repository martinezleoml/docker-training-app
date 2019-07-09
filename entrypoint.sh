#!/usr/bin/env sh

set -xe

export PYTHONPATH=.
export DEBUG="true"

exec gunicorn --bind 0.0.0.0:8000 \
    --workers 5 \
    --threads 1 \
    --timeout 300 \
    --access-logfile - \
    --reload flaskr.wsgi:app
