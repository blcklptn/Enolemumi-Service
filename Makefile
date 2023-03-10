startDocker:
	docker-compose --env-file .env up

startBackend:
	poetry run python3 SourceFiles/enolemumiProject/manage.py runserver

migrate:
	poetry run python3 SourceFiles/enolemumiProject/manage.py migrate

makemigrate:
	poetry run python3 SourceFiles/enolemumiProject/manage.py makemigrations

installReq:
	poetry install --sync