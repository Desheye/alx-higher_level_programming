<<<<<<< HEAD
#!/bin/bash

# MySQL server connection parameters
MYSQL_USER="imgn"
MYSQL_PASSWORD="astro"

# Connect to MySQL server and list all databases
mysql -u "$MYSQL_USER" -p"$MYSQL_PASSWORD" -e "SHOW DATABASES;"

=======
-- Lists all databases of MySQL server
SHOW DATABASES;
>>>>>>> 6381a72c4e30ad10af2fca0f8c31d67a5c7da165
