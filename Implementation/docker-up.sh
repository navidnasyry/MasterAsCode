#!/bin/bash

docker compose -f ./DTAgent/docker-compose.yaml up -d

docker compose -f ./lstm-rul-api/docker-compose.yaml up -d

docker compose -f ./dify/docker/docker-compose.yaml up -d


