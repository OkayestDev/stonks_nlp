# LocalStack and pytest

## Prerequisites

- Docker Compose

We're using docker for local dev as python development on windows is poopy doo doo

    docker-compose up -d

Shell into python docker

    docker exec -it stonks_nlp /bin/bash

## Generating Model

trainer.py is a script to generate an sklearn model under stonks_model (constants.model_filename)
**@todo:**We'll start committing this file

    python src/trainer.py

## Stonks cli

CLI for getting sentiment of tweet

    python -m src.stonks_cli "some real tweet"

Will print out an integer sentiment

## Testing

We're using python's unittest for tests. Shell in (you can use shell.ps1) and run:

    python -m unittest {testfile}
