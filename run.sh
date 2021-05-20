#!/bin/bash

sudo docker-compose down
sudo docker network prune
sudo docker-compose build
sudo docker-compose up -d
rm ~/.ssh/know*
ssh user@192.168.200.2
