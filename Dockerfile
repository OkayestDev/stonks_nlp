FROM python:latest
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
RUN python -m spacy download en_core_web_sm
COPY . /code/
RUN python setup.py install