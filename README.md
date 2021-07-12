# Catana

Simple library management system

## Running dev

```bash
$ uvicorn catana.main:app --reload
```

## Running tests

```bash
$ pytest
```

## Docker
### Building dockerfile 

```bash
$ docker build -t catana .
```
### Running docker container
```bash
$ docker run catana
```
### Running docker compose with postgresql

```bash
$ docker-compose up -d
```
