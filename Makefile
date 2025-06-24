up:
	docker compose up

debug:
	docker compose run --rm --service-ports ecommerce

build:
	docker compose build

migrations:
	docker compose run ecommerce python manage.py makemigrations

migrate:
	docker compose run ecommerce python manage.py migrate
