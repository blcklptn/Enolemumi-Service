startDocker:
	docker-compose --env-file .env up

startBackend:
	poetry run python3 SourceFiles/enolemumiProject/manage.py runserver

migrate:
	poetry run python3 SourceFiles/enolemumiProject/manage.py migrate

installReq:
	poetry install --sync