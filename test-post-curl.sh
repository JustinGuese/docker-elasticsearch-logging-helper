#!/bin/bash
curl --location --request POST 'localhost:5000' \
--header 'Content-Type: application/json' \
--data-raw '{
    "password": "testitest",
    "appname": "testapp",
    "errorjson": {
        "code": 500,
        "errormsg": "example failure"
    }
}'