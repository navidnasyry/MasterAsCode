#!/bin/bash

docker compose -f ./DTAgent/docker-compose.yaml down

docker compose -f ./lstm-rul-api/docker-compose.yaml down

docker compose -f ./dify/docker/docker-compose.yaml down


