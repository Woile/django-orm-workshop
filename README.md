# Django ORM Workshop

> Introduction on how to start using the ORM

## About

In this workshop we are gonna learn how to use the ORM. And how to do some common SQL operations:

Some of the operations

- Insertion
- Updating
- Selecting with join
- Counting
- Agregations
- Sum

## Installation

1. Verify docker is installed in your OS. Run `docker -v` [Docker install](https://docs.docker.com/install/)
1. Verify docker compose is installed. Run `docker-compose -v` [Docker compose install](https://docs.docker.com/compose/install/)
1. Run `make init`

## Usage

### Run the Django server and the Jupyter Notebook

We are gonna use this in the **workshop**

`make run-dev`

#### URLS

Base url: `0.0.0.0:8000/` (with links to djagno tutorials and documentation)

Admin panel: `0.0.0.0:8000/admin`

Jupyter: `0.0.0.0:8888/tree` Token should appear in the log of the docker

### Migrations mini-tutorial

Note: This is done automatically by `make init`, it's just for you to play around

After creating/modifying a model run:

`make makemigrations`

To apply the mirgations:

`make migrate`

To import the data:

`make fixtures`

### Create superuser for the admin panel

`make createsuperuser`


## Presentation

Check [yarn](https://yarnpkg.com/lang/en/docs/install/) is installed.

```bash
yarn install
yarn start
```

Enjoy.
