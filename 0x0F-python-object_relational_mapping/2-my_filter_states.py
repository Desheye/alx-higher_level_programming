#!/usr/bin/python3
"""Displays all values in the states table of hbtn_0e_0_usa where name matches the argument."""
import sys
import MySQLdb

def search_states(username, password, database, state_name):
    """Connects to the MySQL server and searches for states matching the given name."""
    try:
        # Connect to MySQL server
        db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
        cursor = db.cursor()

        # Create SQL query with user input
        query = "SELECT * FROM states WHERE name = '{}' ORDER BY id".format(state_name)

        # Execute query
        cursor.execute(query)

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
    if len(sys.argv) != 5:
        print("Usage: python script.py <username> <password> <database> <state_name>")
    else:
        # Retrieve arguments
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        state_name = sys.argv[4]
        # Call function to search for states
        search_states(username, password, database, state_name)

