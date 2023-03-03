FROM golang:1.19.0-alpine3.16 AS buildando

WORKDIR /app
COPY . /app

RUN go build segundo-exporter.go


FROM alpine:3.16
LABEL maintainer Jeferson Fernando <jeferson@linuxtips.com.br>
LABEL description "Executando o nosso segundo exporter"
COPY --from=buildando /app/segundo-exporter /app/segundo-exporter
EXPOSE 7788
WORKDIR /app
CMD ["./segundo_exporter"]