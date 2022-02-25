#!/bin/sh

if [ "$1" = "local" ]
then
    rm app/config.ini
    cp app/config.example.ini app/config.ini
    docker-compose rm -sf flask
    docker-compose up flask
else
    echo "Please input stage keyword."
    exit
fi