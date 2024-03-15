#!/bin/bash

# MySQL server connection parameters
MYSQL_USER="imgn"
MYSQL_PASSWORD="astro"

# Connect to MySQL server and list all databases
mysql -u "$MYSQL_USER" -p"$MYSQL_PASSWORD" -e "SHOW DATABASES;"

