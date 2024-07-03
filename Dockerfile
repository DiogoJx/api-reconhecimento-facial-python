# syntax=docker/dockerfile:1

FROM python:3.10.3-slim-bullseye

RUN apt-get -y update && \
    apt-get install -y --fix-missing \
    build-essential \
    cmake \
    gfortran \
    git \
    wget \
    curl \
    graphicsmagick \
    libgraphicsmagick1-dev \
    libatlas-base-dev \
    libavcodec-dev \
    libavformat-dev \
    libgtk2.0-dev \
    libjpeg-dev \
    liblapack-dev \
    libswscale-dev \
    pkg-config \
    python3-dev \
    python3-numpy \
    software-properties-common \
    zip \
    default-libmysqlclient-dev \
    sqlite3 \
    vim

WORKDIR /app

RUN chmod 777 -R .

ENV FLASK_APP app.py

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

RUN chmod 777 -R .

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "wsgi:app"]

EXPOSE 8000
