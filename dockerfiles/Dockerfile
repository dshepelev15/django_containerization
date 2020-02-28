FROM python:3.7-slim

WORKDIR /code

COPY requirements.txt ./

RUN apt-get update && apt-get install -y gcc libpq-dev
RUN pip install -r requirements.txt

COPY app/ .

EXPOSE 8000
CMD python manage.py migrate && \
    python manage.py collectstatic --noinput && \
    gunicorn project.wsgi:application --bind 0.0.0.0:8000 --workers=4
