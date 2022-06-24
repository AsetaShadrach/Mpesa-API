FROM python:3.8-slim-buster

WORKDIR /api

COPY . /api

RUN pip install --upgrade pip && pip install -r requirements.txt

EXPOSE 8000

CMD python manage.py makemigrations \
    && python manage.py migrate \
    && python manage.py runserver 0.0.0.0:8000