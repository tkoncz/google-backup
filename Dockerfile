FROM python:3.9.6-slim

RUN mkdir -p /app
WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN python -m pip install -r requirements.txt --no-cache
