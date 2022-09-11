#!/usr/bin/python3
"""
python script that lists all states from the database 
hbtn_0e_0_usa with a name starting with N
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    cursor = db.cursor()
    cmd = """SELECT id, name
          FROM states
          WHERE name LIKE BINARY 'N%' 
          ORDER BY id ASC;"""
    cursor.execute(cmd)
    nStates = cursor.fetchall()

    for state in nStates:
        print(state)
    
    cursor.close()
    db.close()
