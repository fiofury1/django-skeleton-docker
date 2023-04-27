# Django-Skeleton-Docker #

Dockerized version of [Django-Skeleton](https://github.com/fiofury1/django-skeleton) project.

Deployed on [Heroku](https://dj-skel-docker.herokuapp.com/)

## Functionality & Configuration ##
With the exception of the variations/additions below, the project has the same functionality and configuration as [Django-Skeleton](https://github.com/fiofury1/django-skeleton).
- Deployment
     - Docker based deployment to Heroku using heroku.yml.
     - Uses 'dj-database-url' package to parse DATABASE_URL env variable provided by Heroku into settings.DATABASES setting.
- Docker / Docker-Compose
     - Has two containers (web application and database)
     - Run locally using docker-compose.yml
     - Run in production using heroku.yml
     - Dockerfiles
          - Dockerfile.dev => for local development
          - Dockerfile.prod => for production
          - Only difference between files is that .dev includes added packages used for development/debugging.
- Testing
     - Includes only high value, functional testing with Selenium / Chrome / Chrome-Driver
     - Currently only configured to run outside of Docker 
- Database 
     - Local via SQLite or PostgreSQL (with data mount to 'data/' directory.  defined in docker-compose.yml)
          - Run `sudo chown -R $USER:$USER data` to change 'data/' permissions. 
     - Migrations
          - `python manage.py makemigrations` - Run locally.  Migration files stored to repo.
          - `python manage.py migrate` - Manually executed in running container
               - Local:       `docker compose exec web python manage.py migrate`
               - Heroku CLI:  `heroku run python manage.py migrate`
- Static Files
     - Must manually run `collectstatic` in running container
          - Local:       `docker compose exec web python manage.py collectstatic`
          - Heroku CLI:  `heroku run python manage.py collectstatic` (<- Not sure if this is automatically run by Heroku)