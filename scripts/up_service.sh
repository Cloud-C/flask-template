#!/bin/sh

if [ "$1" = "local" ]
then
    rm conf/redis/redis.conf
    cp conf/redis/redis.example.conf conf/redis/redis.conf
    rm conf/fluentd/fluentd.conf
    cp conf/fluentd/fluentd.example.conf conf/fluentd/fluentd.conf
    docker-compose -f services.yml -f services_extra.yml --env-file .env.example up -d
else
    echo "Please input stage keyword."
    exit
fi