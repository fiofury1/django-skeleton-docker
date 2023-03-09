# Pull base image
FROM python:3.10-slim

# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# # Install dependencies (if using pip and requirements.txt)
# COPY ./requirements.txt
# RUN pip install -r requirements.txt

# Install dependencies
RUN pip install pipenv
COPY Pipfile /code
# COPY scripts/install_dependencies.sh /code/scripts/install_dependencies.sh
# RUN chmod u+x ./scripts/install_dependencies.sh && ./scripts/install_dependencies.sh

# For Dev
RUN pipenv install --system --dev --skip-lock
# For Prod
# RUN pipenv install --system --skip-lock

# Copy project
COPY . .