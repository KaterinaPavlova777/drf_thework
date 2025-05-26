#!/bin/bash
set -e

# Ждем доступности базы данных
until PGPASSWORD=$POSTGRES_PASSWORD psql -h "$POSTGRES_HOST" -U "$POSTGRES_USER" -d "$POSTGRES_DB" -c '\q'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

>&2 echo "Postgres is up - executing command"

# Применяем миграции
python manage.py migrate

# Запускаем сервер
exec gunicorn Restapimodel.wsgi:application --bind 0.0.0.0:8000