FROM python:2.7

RUN mkdir p /youtube; exit 0

WORKDIR /youtube

COPY . /youtube

RUN pip install -r packages.txt

CMD python db_migrate.py db init && python db_migrate.py db migrate && python db_migrate.py db upgrade && python app.py

