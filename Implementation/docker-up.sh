#!/bin/bash
export HOST_IP=192.168.24.4

docker compose -f ./DTAgent/docker-compose.yaml up -d

docker compose -f ./lstm-rul-api/docker-compose.yaml up -d

docker compose -f ./dify/docker/docker-compose.yaml up -d

docker compose -f ./motor-dashboard/docker-compose.yaml up -d

docker compose -f ./engine-monitor/docker-compose.yaml up -d


