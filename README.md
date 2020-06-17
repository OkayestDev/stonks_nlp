# LocalStack and pytest

### Windows

    You'll need "Microsoft Visual C++ 14.0" to compile dependencies:
    https://visualstudio.microsoft.com/downloads/
    Be sure to select build tools before installing

## Prerequisites

- Python 3+
- Docker Compose

Create a new python env

    python -m venv .env
    .\.env\Scripts\activate

Install the required pip packages for the project with:

    $ pip3 install -r requirements.txt


## Run Localstack

The easy way is to run LocalStack with docker-compose

Run the LocalStack container in the background with:
  
 \$ docker-compose up -d

Follow the logs with:

    $ docker logs -f localstack

Till you see:

```
...
Waiting for all LocalStack services to be ready
Ready.
```

## Run tests

A simple test that creates, invokes, and then tears down a simple Lambda is provided.

To run the test, use the following commands within the root of the project:

```
$ cd lambda/basic_lambda
$ pytest -s .
```
