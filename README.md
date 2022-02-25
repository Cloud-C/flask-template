
## Setup Submodule

```
git submodule init
git submodule update
cd app/common
git checkout <branch>
```

### Create Docker Network

if network is not existed. please create it.

`docker network create flask_network`

### Stage Tags

1. `local`

## Scripts

+ Up Services

`sh scripts/up_service.sh <stage_tag>`

+ Down Services

`sh scripts/down_service.sh <stage_tag>`

+ Run API Server

`sh scripts/run.sh <stage_tag>`

+ Stop API Server

`sh scripts/stop.sh`

+ Build DB & Rebuild DB

`sh scripts/rebuild.sh <stage_tag>`

+ Testing

`sh scripts/run_test.sh`


---

## Initial Steps

```
docker network create flask_network
sh scripts/up_service.sh <stage_tag>
sh scripts/run.sh <stage_tag>
```
