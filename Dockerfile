## Pull base image
#FROM python:3.10
## set work directory
#WORKDIR /app
#
## set environment variables
#ENV PIP_DISABLE_PIP_VERSION_CHECK 1
#ENV PYTHONDONTWRITEBYTECODE 1
#ENV PYTHONUNBUFFERED 1
#
## install dependencies
##COPY ../requirements.txt requirements.txt
##RUN pip3 install -r requirements.txt
#COPY ./requirements.txt .
#RUN pip install -r requirements.txt
##CMD ['python','manage.py','collectstatic']
#COPY . /app
#


# syntax=docker/dockerfile:1
FROM python:3.10-alpine

#ENV KINOCMS=/usr/src/kino_cms
#
#RUN mkdir -p $KINOCMS

WORKDIR /usr/src/kino_cms

# set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN adduser -D vlad
USER vlad

RUN pip install --upgrade pip
COPY --chown=vlad:vlad ./requirements.txt /usr/src/kino_cms/
#COPY ./requirements.txt $KINOCMS/

RUN pip install --user -r requirements.txt
#RUN pip install -r requirements.txt

ENV PATH="/home/vlad/.local/bin:${PATH}"
# copy project
COPY . /usr/src/kino_cms/

