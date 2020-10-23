# set base image (host OS)
FROM python:3.7.3-slim

# upgrade pip
RUN pip install --upgrade pip

# build the working directory
RUN mkdir /app

# set the working directory in the container
WORKDIR /app

# copy the dependencies file to the working directory
ADD requirements.txt /app

# install dependencies
RUN pip install -r requirements.txt --no-cache-dir

# copy the content of the local src directory to the working directory
ADD . /app

EXPOSE 5000

# for simple testing- for production comment this
ENTRYPOINT ["python", "app/app.py"]

# for real production using gunicorn- comment it if doing it for testing only
# ENTRYPOINT ["gunicorn", "--config", "gunicorn_config.py", "app.wsgi:app"]