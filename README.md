# Django ORM Workshop

> Introduction on how to start using the ORM

## Demo

## Installation

1. Verify docker is installed in your OS. Run `docker -v` [Docker install](https://docs.docker.com/install/)
1. Verify docker compose is installed. Run `docker-compose -v` [Docker compose install](https://docs.docker.com/compose/install/)
1. Run `make init`

## Usage

### Create superuser for the admin panel

`make createsuperuser`

### Run the Django server and the notebook (used in the workshop)

This is useful to access the admin

`make run-dev`

#### URLS

Base url: `0.0.0.0:8000/` (with links to djagno tutorials and documentation)

Admin panel: `0.0.0.0:8000/admin`

Jupyter: `0.0.0.0:8888/tree` Token should appear in the log of the docker

### Migrations mini-tutorial

After creating/modifying a model run

`make makemigrations`

To apply the mirgations:

`make migrate`

## Presentation

Check [yarn](https://yarnpkg.com/lang/en/docs/install/) is installed.

```bash
yarn install
yarn start
```

Enjoy.
