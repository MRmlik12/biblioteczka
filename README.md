# Catana
[![Test & Lint](https://github.com/MRmlik12/catana/actions/workflows/test-lint.yml/badge.svg)](https://github.com/MRmlik12/catana/actions/workflows/test-lint.yml)
[![codecov](https://codecov.io/gh/MRmlik12/catana/branch/develop/graph/badge.svg?token=jv5OPgc9j7)](https://codecov.io/gh/MRmlik12/catana)

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
