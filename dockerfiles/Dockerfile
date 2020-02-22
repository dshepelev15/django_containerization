FROM python:3.7-slim

WORKDIR /code

COPY requirements.txt ./

RUN pip install pip --upgrade && \
    pip install -r requirements.txt

COPY app/ .

CMD python manage.py migrate && python manage.py runserver 0:8000
