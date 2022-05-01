FROM python:3.9.12

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY pyproject.toml .
COPY poetry.lock .

RUN apt-get update && apt-get -y install cron
RUN pip install --upgrade pip && \
    pip install --no-cache-dir poetry==1.0.3 && \
    poetry export --without-hashes -f requirements.txt -n -o requirements.txt && \
    pip uninstall --yes poetry && \
    pip install -r requirements.txt

COPY . /app

RUN python manage.py collectstatic --no-input --no-color
