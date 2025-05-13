# Используем официальный образ Python
FROM python:3.12-slim

# Устанавливаем переменные окружения
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PIP_NO_CACHE_DIR=1
ENV PATH="/root/.local/bin:${PATH}"

# Устанавливаем системные зависимости
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем Poetry
RUN pip install --upgrade pip && \
    pip install poetry

# Настраиваем Poetry (не создавать виртуальные окружения в контейнере)
RUN poetry config virtualenvs.create false

# Создаем и переходим в рабочую директорию
WORKDIR /code

# Копируем файлы зависимостей
COPY pyproject.toml poetry.lock ./

# Устанавливаем зависимости через Poetry
RUN poetry install --no-interaction --no-ansi --only main

# Копируем весь проект
COPY . .

# Команда запуска
EXPOSE 8000
CMD ["gunicorn", "Restapimodel.wsgi:application", "--bind", "0.0.0.0:8000"]