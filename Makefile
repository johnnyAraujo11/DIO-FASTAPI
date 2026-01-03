run: 
	@uvicorn workout_api.main:app --reload

requirements:
	@pip freeze > requirements.txt

# lembrando que esses dois comandos abaixo são referentes ao sistema operacional, windows
create-migrations:
	set PYTHONPATH=src && python -m alembic revision --autogenerate -m "initial migration"

run-migrations:
	set PYTHONPATH=src && python -m alembic upgrade head	