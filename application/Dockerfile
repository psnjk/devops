# syntax=docker/dockerfile:1

FROM python:3.8-alpine

WORKDIR /

RUN pip3 install --upgrade pip

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt --no-cache-dir

RUN pip3 install requests

COPY . .

