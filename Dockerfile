FROM python:3.8
LABEL maintainer="lambrosopos@gmail.com"

ENV APP_DIR /blog_app
WORKDIR $APP_DIR
EXPOSE 8000

COPY ./requirements.txt requirements.txt
RUN python -m pip install -r requirements.txt

COPY ./blog_site .
CMD ["gunicorn", "blog_site.wsgi"]
