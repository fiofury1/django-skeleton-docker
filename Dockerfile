#Helpful Docker CLI commands:
#	To build image:  					>>docker image build -t <image>:<tag> .  ex.  docker image build -t teslaforce:add_feature .
#	To run container:  					>>docker container run -it -p 8000:80 <image>:<tag>
# 	To list images:  					>>docker image ls
#	To remove image:					>>docker rmi <id>
#	To list running containers:			>>docker container ls
#	To list running/stopped containers:	>>docker container ls -a
#	To remove container:				>>docker rm <id>


# Pull base image
FROM python:3.9-slim
# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# Set work directory.  Commands get executed relative to the specified WORKDIR. 
WORKDIR /code
# Install dependencies
COPY Pipfile Pipfile.lock /code/
RUN pip install pipenv && pipenv install --system
# Copy project
COPY . /code/

# To run Django development server build image with CMD below then run:    
#   >>docker container run -it -p 8000:8000 <image>:<tag>
CMD python manage.py runserver 0.0.0.0:8000