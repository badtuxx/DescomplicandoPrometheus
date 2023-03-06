FROM python:3.8-slim

LABEL maintainer Jeferson Fernando <jeferson@linuxtips.com.br>
LABEL description "Dockerfile para criar o nosso primeiro exporter para o Prometheus"

COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt

CMD python3 exporter.py