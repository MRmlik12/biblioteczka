FROM python:3.8.11

WORKDIR /app

COPY . .

RUN pip3 install -r requirements/base.txt
EXPOSE 5000
ENTRYPOINT uvicorn catana.main:app