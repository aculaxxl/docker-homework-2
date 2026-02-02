d-homework-i-run:
	docker-compose build
	docker-compose up

d-homework-i-purge:
	docker-compose down --rmi all -vO

