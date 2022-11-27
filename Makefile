run-db:
	docker run --name calendar-db-postgres -p 5432:5432 -e POSTGRES_PASSWORD=mysuperpassword -e POSTGRES_DB=calendar_db -v ${PWD}/db_data:/var/lib/postgresql/data -d postgres