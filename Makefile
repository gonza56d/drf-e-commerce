up:
	docker compose up

build:
	docker compose build

migrations:
	docker compose run ecommerce python manage.py makemigrations

migrate:
	docker compose run ecommerce python manage.py migrate
