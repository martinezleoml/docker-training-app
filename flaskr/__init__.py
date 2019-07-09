#!/usr/bin/env python

from flask import Flask, send_from_directory, render_template
import os
import redis
import socket


app = Flask(__name__)
hostname = socket.gethostname()

if "DEBUG" in os.environ:
    app.debug = True


@app.errorhandler(500)
def error(e):
    return render_template('error.html',
        hostname=hostname, error=e), 500


@app.route("/")
def index():
    redis_error = False
    counter = 0

    try:
        redis_client = redis.Redis(os.environ.get('REDIS_HOST'),
                                   socket_timeout=1,
                                   socket_connect_timeout=1)

        redis_client.incr('counter', 1)
        counter = redis_client.get('counter') or 0
    except redis.exceptions.ConnectionError:
        redis_error = True

    return render_template(
        "index.html",
        hostname=hostname,
        counter=int(counter),
        redis_error=redis_error
    )


@app.route("/assets/<path:path>")
def assets(path):
    return send_from_directory("assets", path)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
