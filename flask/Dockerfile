FROM python:3.6

ENV PYTHONUNBUFFERED=1

RUN mkdir /flask-grpc
WORKDIR  /flask-grpc

COPY . . 
RUN pip install --upgrade pip 
RUN pip install -r requirements.txt

CMD python app.py