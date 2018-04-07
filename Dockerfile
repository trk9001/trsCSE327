FROM python:3
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
COPY ./requirements.txt /code/requirements.txt
COPY . /code/

WORKDIR /code/
RUN pip install -r requirements.txt
