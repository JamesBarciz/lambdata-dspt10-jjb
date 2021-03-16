# Dockerfile for Lambdata application
FROM python:latest

WORKDIR /lambdata-package

ADD lambdata/helper_functions.py .

COPY requirements.txt .

RUN pip install -r requirements.txt

CMD [ "ls", "-a" ]