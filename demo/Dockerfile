FROM python:3.7.1-alpine3.8

# Add testing and main repos (which include many of our OS deps)
RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories
RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/main" >> /etc/apk/repositories
RUN echo "ipv6" >> /etc/modules

RUN apk update
RUN apk add --upgrade apk-tools

RUN apk add --no-cache \
            postgresql postgresql-dev libxslt-dev pkgconfig \
            py3-setuptools alpine-sdk python3-dev python-dev \
            binutils curl proj4-dev bash

# Create unprivileged user
RUN adduser -D -g '' myuser

# No pyc files
ENV PYTHONDONTWRITEBYTECODE 1

# Better output
ENV PYTHONUNBUFFERED 1

RUN which python
RUN /bin/bash -c "pip install pip -U"

# set working directory to /demo/
WORKDIR /demo/

# COPY deps
COPY requirements.txt requirements.txt


# Instal deps
RUN ["python", "-m", "pip", "install", "-r", "requirements.txt"]

COPY wait-for-postgres.sh /demo/wait-for-postgres.sh
ENTRYPOINT ["/demo/wait-for-postgres.sh", "db"]

CMD ["run_api.sh"]
