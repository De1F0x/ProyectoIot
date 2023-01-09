FROM python:3.9

RUN apt -qq -y update \
&& apt -qq -y upgrade

RUN pip install mysql-connector-python flask

WORKDIR /usr/src

COPY . .

EXPOSE 4000
