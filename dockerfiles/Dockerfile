FROM python:3.7-slim

WORKDIR /code

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY app/ .

EXPOSE 8000
CMD python manage.py migrate && python manage.py runserver 0:8000
