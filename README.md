# Fastapi JWT Token Authentication

Exec terminal of postgres, loging into the database:
psql -h postgres -p 5432 -U paul -d fastapi_auth

\conninfo
You are connected to database "fastapi_auth" as user "paul" on host "postgres" (address "172.18.0.2") at port "5432".

- https://www.sqlshack.com/getting-started-with-postgresql-on-docker/
- https://www.cybertec-postgresql.com/en/show-tables-in-postgresql-whats-wrong-with-it/?gclid=CjwKCAiAkp6tBhB5EiwANTCx1FnzJUAFv8OKALkuA64vTm-ivz6YGTFHm1NOgJE4txpfQM_yOn9tEhoCQPQQAvD_BwE
- https://medium.com/@johnidouglasmarangon/using-migrations-in-python-sqlalchemy-with-alembic-docker-solution-bd79b219d6a


    command: bash -c "cd app/database && alembic upgrade head && cd ../.. && python app/main.py"
