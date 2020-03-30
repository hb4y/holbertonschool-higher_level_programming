#!/usr/bin/python3
"""
lists all states with a name starting with N (upper N)
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
    cur.execute("SELECT * \
                 FROM states \
                 WHERE name LIKE BINARY 'N%' \
                 ORDER BY id ASC")
    query = cur.fetchall()
    for row in query:
        print(row)

    cur.close()
    conn.close()
