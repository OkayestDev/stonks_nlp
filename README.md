# LocalStack and pytest

## Prerequisites

- Docker Compose

We're using docker for local dev as python development on windows is poopy doo doo

    docker-compose up -d

Shell into python docker

    docker exec -it stonks_nlp /bin/bash

## Localstack

Follow the logs with:

    $ docker logs -f localstack

Until you see:

    ```
    ...
    Waiting for all LocalStack services to be ready
    Ready.
    ```
