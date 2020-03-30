#!/usr/bin/python3
"""
 displays all cities
"""
import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: {} username password database_name".format(sys.argv[0]))
        exit(1)

    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])

    cur = conn.cursor()
    cur.execute("SELECT c.id, c.name, s.name \
                 FROM states s, cities c \
                 WHERE s.id = c.state_id \
                 ORDER BY id ASC")

    query = cur.fetchall()
    for row in query:
        print(row)

    cur.close()
    conn.close()
