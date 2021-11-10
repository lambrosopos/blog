FROM python:3.8
LABEL maintainer="lambrosopos@gmail.com"

ENV APP_DIR /blog_app
WORKDIR $APP_DIR
EXPOSE 8000

COPY ./requirements.txt requirements.txt
RUN python -m pip install -r requirements.txt

COPY ./gunicorn_start ./gunicorn_start
RUN chmod u+x ./gunicorn_start

COPY ./blog_site .
