FROM python:3.7-alpine

RUN apk update && \
    apk add --virtual build-deps gcc python-dev musl-dev && \
    apk add postgresql-dev
RUN pip install psycopg2

ADD restFlaskApp /restFlaskApp
WORKDIR /restFlaskApp
RUN pip install -r requirements.txt
CMD python app.py