FROM debian:latest

RUN apt-get -y update \
  && apt-get -y install python python-dev python-pip \
  && pip install -U celery[redis] \
  && pip install flask \
  && pip install gunicorn \
  && rm -rf /var/lib/apt/lists/*

ENV PYTHON_PATH /app
RUN mkdir /app
WORKDIR /app

EXPOSE 80 443

RUN useradd -ms /bin/bash admin

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:80", "server:app"]
