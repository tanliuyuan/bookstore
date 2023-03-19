FROM ubuntu:jammy

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV DEBIAN_FRONTEND noninteractive
ENV PYTHONDONTWRITEBYTECODE=1
ENV FLASK_APP=app/main.py

# System dependencies
RUN apt update && apt upgrade -y
RUN apt -y install apt-utils \
    python3-distutils \
    curl \
    && apt clean
RUN curl -Ss https://bootstrap.pypa.io/get-pip.py | python3

# Python dependencies
WORKDIR /bookstore
COPY . .
RUN pip3 install -r requirements.txt
