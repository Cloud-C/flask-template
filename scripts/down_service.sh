#!/bin/sh

if [ "$1" = "local" ]
then
    docker-compose -f services.yml -f services_extra.yml --env-file .env.example down
else
    echo "Please input stage keyword."
    exit
fi