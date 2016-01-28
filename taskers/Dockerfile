FROM debian:latest

RUN apt-get -y update \
  && apt-get -y install python python-dev python-pip \
  && pip install -U celery[redis] \
  && rm -rf /var/lib/apt/lists/*

ENV PYTHON_PATH /app
RUN mkdir /app
WORKDIR /app

RUN useradd -ms /bin/bash celery
USER celery

CMD ["celery", "-A", "tasks", "worker", "--loglevel=info"]
