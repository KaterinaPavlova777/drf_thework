FROM python:3.12-slim

# Устанавливаем переменные окружения
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PIP_NO_CACHE_DIR=1

# Устанавливаем системные зависимости
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем Poetry глобально
RUN pip install --upgrade pip && \
    pip install poetry && \
    poetry config virtualenvs.create false

# Рабочая директория
WORKDIR /code

# Копируем только файлы зависимостей
COPY pyproject.toml poetry.lock ./

# Устанавливаем зависимости без текущего проекта
RUN /root/.local/bin/poetry install --no-interaction --no-ansi --only main --no-root

# Копируем весь проект
COPY . .

# Указываем полный путь к poetry для гарантии
ENV PATH="/root/.local/bin:${PATH}"

# Команда запуска (используем прямой вызов gunicorn)
EXPOSE 8000
CMD ["gunicorn", "Restapimodel.wsgi:application", "--bind", "0.0.0.0:8000"]