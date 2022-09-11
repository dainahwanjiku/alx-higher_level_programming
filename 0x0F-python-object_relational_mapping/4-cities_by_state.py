#!/usr/bin/python3
"""
python script that lists all cities from the
database hbtn_0e_4_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    cursor = db.cursor()
    cmd = """SELECT cities.id, cities.name, states.name
          FROM states
          INNER JOIN cities ON states.id = cities.state_id
          ORDER BY cities.id ASC"""
    cursor.execute(cmd)
    allcities = cursor.fetchal()
    
    for city in allCities:
        print(city)

    cursor.close()
    db.close()
