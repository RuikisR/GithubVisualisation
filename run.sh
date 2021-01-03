#!/bin/bash

docker build -t github-visualiser .
docker run -t -p 5000:5000 github-visualiser