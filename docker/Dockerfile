FROM python:3.11-alpine

RUN apk add --no-cache gcc musl-dev linux-headers

RUN pip install poetry

WORKDIR /app

COPY . /app

RUN poetry install
