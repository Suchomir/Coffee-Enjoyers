FROM python:3.8-alpine

RUN apk update \
  && apk add --update --no-cache git openssh-client \
  && addgroup -S -g 1001 coffee \
  && adduser -S -D -h /home/coffee -u 1001 -G coffee coffee

WORKDIR /app

COPY --chown=root:root src/ .
RUN pip3 install -r requirements.txt && pip3 install gunicorn

USER coffee
EXPOSE 8000
CMD ["gunicorn", "--threads", "8", "--bind", "0.0.0.0:8000", "--access-logfile", "-", "app:app"]
