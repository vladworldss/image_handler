### Docker

#### Quickstart


1. Run docker-compose
```shell script
docker-compose up -d
```

Sometimes DB running not fast enough and backend can't connect to it upon first run. 
Just restart backend container in order to fix it.
```shell script
docker-compose restart backend
```

#### Connecting To Database
```shell script
docker-compose exec db psql -U image_handler
```
Db credentials for local (not-in-docker) deploy:

| cred | value     |
|------|-----------|
| host | localhost |
| port | 6432 |
| user | billing |
| password | billing |
| database | billing |

### Extra
* Check docker started.
  ```shell script
  docker-compose ps
  ```
  

* Cleaning up all docker containers, images, volumes, etc. (for current project only).
  ```shell script
  docker-compose down --volumes --rmi local --remove-orphans
  ```

* Rebuilding single container.
  ```shell script
  docker-compose stop backend
  docker-compose up -d --build backend
  ```

  