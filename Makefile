bash:
	docker-compose run --user=$(shell id -u) ${service} bash

build-images:
	docker-compose build

clean: stop remove

createsuperuser:
	docker-compose run api python manage.py createsuperuser

dev:
	docker-compose up

fixtures:
	docker-compose run api python manage.py loaddata humanresources

init: clean build-images migrate fixtures dev

makemigrations:
	# example make makemigrations app=review
	docker-compose run api python manage.py makemigrations ${app}

migrate:
	# example make migrate app=review num=0004
	docker-compose run api python manage.py migrate ${app} ${num} ${options}

# Removes old containers, free's up some space
remove:
	# Try this if this fails: docker rm -f $(docker ps -a -q)
	docker-compose rm --force -v

stop:
	docker-compose stop

run-dev: build-images migrate dev
