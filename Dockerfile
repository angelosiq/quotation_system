FROM python:3.9.12

WORKDIR /app

COPY pyproject.toml .
COPY poetry.lock .

RUN pip install --upgrade pip && \
    pip install --no-cache-dir poetry==1.0.3 && \
    poetry export --without-hashes -f requirements.txt -n -o requirements.txt && \
    pip uninstall --yes poetry && \
    pip install -r requirements.txt

COPY . /app

RUN python manage.py collectstatic --no-input --no-color

CMD gunicorn probresult.wsgi:application -w 5 \
    --threads 8 -b :$8005 --timeout 900 \
    --log-level=debug --limit-request-line 0
