FROM python:3.11.4-slim-bullseye
COPY ./requirements.txt /requirements.txt
RUN pip install -U pip && pip install -r requirements.txt
RUN rm -f requirements.txt
RUN pip cache purge
COPY . /app
WORKDIR /app