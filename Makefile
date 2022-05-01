build:
	docker-compose up -d --build
	docker-compose exec web python manage.py migrate
	docker-compose exec web python manage.py set_up_data
	docker-compose exec web python manage.py crontab add
