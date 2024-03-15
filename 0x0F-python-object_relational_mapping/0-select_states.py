#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """
import sys

import MySQLdb


def list_states(username, password, database):
    """List states from the database."""
    # Connect to MySQL server
    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )
        cursor = db.cursor()
    except MySQLdb.Error as error:
        print("Error connecting to MySQL:", error)
        return

    # Execute query
    try:
        cursor.execute("SELECT * FROM states ORDER BY id")
        states = cursor.fetchall()
        print("All states:")
        for state in states:
            print(state)
    except MySQLdb.Error as error:
        print("Error executing MySQL query:", error)
    finally:
        # Close cursor and database connection
        cursor.close()
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

