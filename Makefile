startDocker:
	docker-compose --env-file .env

startBackend:
	poetry run python3 SourceFiles/enolemumiProject/manage.py runserver

migrate:
	poetry run python3 SourceFiles/enolemumiProject/manage.py migrate