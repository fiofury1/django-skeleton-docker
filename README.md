# Django-Skeleton-Docker #

Dockerized version of [Django-Skeleton](https://github.com/fiofury1/django-skeleton) project.

Deployed on [Heroku](https://dj-skel-docker.herokuapp.com/)

## Functionality & Configuration ##
With the exception of the variations/additions below, the project has the same functionality and configuration as [Django-Skeleton](https://github.com/fiofury1/django-skeleton).
- Deployment
     - Docker based deployment to Heroku using heroku.yml.
     - Follows instructions found in <u>Django for Professionals</u> by William Vincent.  In general, steps include:
          1. Create a heroku.yml file. 
          2. Create a new project in Heroku (can use CLI or Website).
          3. Assign environment variables in Heroku (called Config variables in Heroku).</br>
               If using PostgreSQL, Heroku will automatically create and set 'DATABASE_URL' when you add the Postgres add-on.  
          4. Set Heroku stack to 'container'</br>
               `$ heroku stack:set container -a <app-name>`  Ex.  `$ heroku stack:set container -a mysterious-hollows-62532`
          5. Add Heroku Postgres add-on to Heroku.  (can be done through CLI or Website)
          6. Add Heroku as remote to local git project.</br>
               `$ heroku git:remote -a <app-name>`  Ex.  `$ heroku git:remote -a mysterious-hollows-62532`
          7. Push code to Heroku.</br>
               `$ git push heroku main`
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
          - Run `$ sudo chown -R $USER:$USER data` to change 'data/' permissions. 
     - Migrations
          - `$ python manage.py makemigrations` - Run locally.  Migration files stored to repo.
          - `$ python manage.py migrate` - Manually executed in running container
               - Local:       `$ docker compose exec web python manage.py migrate`
               - Heroku CLI:  `$ heroku run python manage.py migrate`
- Static Files
     - Local Docker:  Must manually run `collectstatic` in running container
          - `$ docker compose exec web python manage.py collectstatic`
     - Heroku:  Run via command issued in heroku.yml