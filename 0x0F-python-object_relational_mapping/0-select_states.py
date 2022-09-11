#!/usr/bin/python3
"""
python script that lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', 
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2], 
                         db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT id, name FROM states ORDER BY id ASC")
    allStates = cursor.fetchall()

    for state in allStates:
        print(state)

    cursor.close()
    db.close()
