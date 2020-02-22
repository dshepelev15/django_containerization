FROM python:3.7-slim

WORKDIR /code

# нужно поставить gcc для библиотеки psycopg2
RUN apt-get update && apt-get install -y gcc libpq-dev

COPY requirements.txt ./

RUN pip install pip --upgrade && \
    pip install -r requirements.txt

COPY app/ .

EXPOSE 8000
CMD python manage.py migrate && python manage.py runserver 0:8000
