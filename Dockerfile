FROM python:3-alpine

WORKDIR /app

COPY requirements.txt .
RUN pip install gunicorn && \
    pip install -r requirements.txt

COPY . .

EXPOSE 8000
ENTRYPOINT ["/bin/sh", "-c", "/app/entrypoint.sh"]
