FROM python:3.10

RUN apt-get update && apt-get install -y \
    postgresql-client

WORKDIR /app

COPY pyproject.toml poetry.lock /app/

RUN pip install poetry && poetry install --no-root

COPY . /app

ENV POSTGRES_HOST=localhost \
    POSTGRES_PORT=5432 \
    POSTGRES_DB=olimpia \
    POSTGRES_USER=olimpia \
    POSTGRES_PASSWORD=12345

CMD ["python", "my_select.py"]
