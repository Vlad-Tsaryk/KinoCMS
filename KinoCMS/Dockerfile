# Pull base image
FROM python:3.10
# set work directory
WORKDIR /app

# set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY ../requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# copy project
COPY .. .

