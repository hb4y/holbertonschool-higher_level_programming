#!/usr/bin/python3
"""
 displays all values in the states where name matches the argument
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
    stmt = "SELECT * \
            FROM states \
            WHERE BINARY name = '{}' \
            ORDER BY id ASC".format(sys.argv[4])

    cur.execute(stmt)
    query = cur.fetchall()
    for row in query:
        print(row)

    cur.close()
    conn.close()
