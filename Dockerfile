FROM python:2.7

RUN mkdir p /youtube; exit 0

WORKDIR /youtube

COPY . /youtube

RUN apt-get -y install cron & echo 'y'

RUN pip install -r packages.txt

# The following commands for making cron jobs, reference https://github.com/Ekito/docker-cron/blob/master/Dockerfile

ADD crontab /etc/cron.d/hello-cron

RUN chmod 0644 /etc/cron.d/hello-cron

RUN touch /var/log/cron.log

RUN apt-get update

RUN apt-get -y install cron

CMD cron && tail -f /var/log/cron.log


