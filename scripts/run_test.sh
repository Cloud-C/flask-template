
docker exec -it flask-postgres psql -U postgres -c 'DROP DATABASE flask_test;'
docker exec -it flask-postgres psql -U postgres -c 'CREATE DATABASE flask_test;'

docker-compose rm -sf flask_test
docker-compose --env-file .env.example up -d flask_test

docker exec -it flask-template-test bash -c "rm app/config.ini"
docker exec -it flask-template-test bash -c "cp app/config.test.ini app/config.ini"
docker exec -it flask-template-test bash -c "pytest --rootdir=tests"

docker exec -it flask-template-test bash -c "cp app/config.example.ini app/config.ini"
docker-compose rm -sf flask_test
