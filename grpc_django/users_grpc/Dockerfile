FROM python:3.6

ENV PYTHONUNBUFFERED=1

RUN mkdir /users

WORKDIR /users

COPY . . 
RUN pip install --upgrade pip 
RUN pip install -r requirements.txt