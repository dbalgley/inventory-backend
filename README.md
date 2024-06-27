# inventory-backend
The backend component of the qr-enabled home inventory web application, including the DB component

Dev Env Setup:
1. sudo apt-get install postgresql postgresql-contrib libpq-dev python3-dev
2. sudo service postgresql start
3. sudo -i -u postgres
4. createuser --interactive (inventory_user, n, n, n)
5. psql
6. ALTER USER inventory_user WITH PASSWORD 'scavenger';
7. \q
8. createdb inventory_db
9. psql
10. GRANT ALL PRIVILEGES ON DATABASE inventory_db TO inventory_user;
11. \q
12. exit
