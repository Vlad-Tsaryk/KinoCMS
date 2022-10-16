# syntax=docker/dockerfile:1
FROM python:3.10-alpine

WORKDIR /home/app/KinoCMS

# set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN pip install --upgrade pip
# copy project
COPY . /home/app/KinoCMS
RUN pip install -r requirements.txt
RUN apk update
RUN apk install gettext -y