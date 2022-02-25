 if [ "$1" = "local" ]
 then
     docker exec -it flask-postgres psql -U postgres -c 'DROP DATABASE flask;'
     docker exec -it flask-postgres psql -U postgres -c 'CREATE DATABASE flask;'
     docker-compose up -d flask_build
 else
     echo "Please input stage keyword."
     exit
 fi

if [ "$1" = "local" ]
then
    docker exec -it flask-template-build bash -c 'rm app/config.ini'
    docker exec -it flask-template-build bash -c  'cp app/config.example.ini app/config.ini'
else
    echo "Please input stage keyword."
    exit
fi

docker exec -it flask-template-build bash -c 'python scripts/manage.py db init'
docker exec -it flask-template-build bash -c 'python scripts/manage.py db migrate'
docker exec -it flask-template-build bash -c 'python scripts/manage.py db upgrade'

docker-compose rm -sf flask_build
