#!/usr/bin/python3
"""Lists all states with a name starting with 'N' from the database hbtn_0e_0_usa."""
import sys
import MySQLdb

def list_states(username, password, database):
    """Connects to the MySQL server and lists states with names starting with 'N'."""
    try:
        # Connect to MySQL server
        db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
        cursor = db.cursor()

        # Execute query
        cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")

        # Fetch all results
        states = cursor.fetchall()

        # Display results
        for state in states:
            print(state)

    except MySQLdb.Error as e:
        print("Error connecting to MySQL:", e)

    finally:
        # Close cursor and database connection
        if 'cursor' in locals():
            cursor.close()
        if 'db' in locals():
            db.close()

if __name__ == "__main__":
    # Check if correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
    else:
        # Retrieve arguments
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        # Call function to list states
        list_states(username, password, database)

