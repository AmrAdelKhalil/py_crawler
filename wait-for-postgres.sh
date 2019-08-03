#!/bin/sh
# wait-for-postgres.sh

sleep 10 # Wait a little bit for postgres

bash -c "python db_migrate.py db init"
bash -c "python db_migrate.py db migrate"
bash -c "python db_migrate.py db upgrade" 
bash -c "python app.py" -D
