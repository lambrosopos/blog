FROM python:3.8
WORKDIR /blog_app
COPY requirements.txt requirements.txt
RUN python -m pip install -r requirements.txt
COPY ./blog_site .
EXPOSE 8000
CMD ["python", "manage.py", "runserver"]
