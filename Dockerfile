FROM python:3.11-slim

RUN apt update; apt-get install -y gettext libgdal-dev

WORKDIR /code

ADD requirements.txt /code/requirements.txt
RUN pip cache purge
RUN pip install -r requirements.txt

ADD ./ /code
