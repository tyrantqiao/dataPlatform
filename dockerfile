FROM python:3.6
LABEL maintainer="tyrantqiao tyrantqiao@gmail.com"
ENV PYTHONUNBUFFERED 1
RUN mkdir /backend
WORKDIR /backend
COPY requirements.txt /backend/
RUN pip3 install -r /backend/requirements.txt
ADD . /backend/

