Super simple, easy Elasticsearch logging using an "inbetween" Flask server that receives POST requests and saves them to Elasticsearch. 

# Description

Your program -> Elasticsearch Logging Helper (this) -> Elasticsearch

Why? I needed something for easy logging to Elasticsearch, and did not want to install the elasticsearch package in every module I am writing, so instead I am just passing the application password with a post request that almost every language should support. E.g. you can easily integrate this into your code, which can be seen in the `example-code.py` file. 

# Usage

Check out the docker-compose on how to deploy this to your Kubernetes / Docker Cluster.

## docker-compose

`docker-compose up`

```
version: "3"
services:
  es_logger:
    image: guestros/elasticsearch-logger-endpoint:latest
    # build: .
    # depends_on: 
    #   - elasticsearch
    container_name: es_logger
    restart: always
    ports:
      - 5000:5000
    environment:
      - ES_HOST="http://elasticsearchurl:9200/"
      - ES_USER=elastic
      - ES_PW=changeme
      - AUTH_PW=testitest # this one is for the application to check if a user is authenticated to log in
```

## kubernetes

`kubectl apply -f kubernetes/`

Check out the `kubernetes` folder for an example