build:
	docker compose -f local.yml up --build -d --remove-orphans

down:
	docker compose -f local.yml down

up:
	docker compose -f local.yml up -d

show-logs:
	docker compose -f local.yml logs

show-logs-api:
	docker compose -f local.yml logs api

makemigrations:
	docker compose -f local.yml run --rm api python backend/manage.py makemigrations

migrate:
	docker compose -f local.yml run --rm api python backend/manage.py migrate

collectstatic:
	docker compose -f local.yml run --rm api python backend/manage.py collectstatic --no-input --clear

superuser:
	docker compose -f local.yml run --rm api python backend/manage.py createsuperuser

down-v:
	docker compose -f local.yml down -v