server:
	poetry run python manage.py runserver


migrations:
	poetry run python manage.py makemigraetions

migrate:
	poetry run python manage.py migrate

superuser:
	poetry run python manage.py createsuperuser