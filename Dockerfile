FROM python:2.7

RUN mkdir p /youtube; exit 0

WORKDIR /youtube

COPY . /youtube

RUN pip install -r packages.txt


