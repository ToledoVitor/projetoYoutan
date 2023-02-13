FROM python:3
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

ADD ./youtan_django/requirements.txt /code/
RUN pip install -r requirements.txt
ADD ./youtan_django /code/
