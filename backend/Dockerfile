FROM python:3.12-slim

WORKDIR /test-task

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=false \
    POETRY_NO_INTERACTION=1

RUN apt update; apt install -y netcat-openbsd

COPY . .

RUN pip install poetry && poetry install --no-root --no-directory

RUN chmod +x entrypoint.sh