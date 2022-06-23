# lab-pro-management-system
Lab management system for managing the laboratory.

## Development Setup

Clone the project and change directory to ``lab-pro-management-system``
```
git clone git@github.com:enoskyeza/lab-pro-management-system.git

cd lab-pro-management-system
```

Inside the ``lab-pro-management-system`` directory build the docker containers for the project and start django server
```
docker-compose up -d --build
```

## Development Common commands

### Execute Django commands

### start docker services and django server
```
# start docker in foreground
docker-compose up

# start docker in background
docker-compose up -d
```

### follow docker django service logs
```
docker-compose logs -f web
```

### follow docker logs for any other service
```
docker-compose logs -f <service>
```

### execute commands inside docker django web service
```
docker-compose exec web bash
```

### execute commands inside any other docker service
```
docker-compose exec <service> bash
```

#### create new django app
```
docker-compose run web django-admin startapp core
```

### executing manage.py commands
```
docker-compose run web python manage.py <command>
```

### restart docker and all services
```
docker-compose restart
```

### shutdown docker and all services
```
docker-compose down
```