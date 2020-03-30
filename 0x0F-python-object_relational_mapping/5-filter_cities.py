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
    state = sys.argv[4]
    stmt = "SELECT DISTINCT c.id, c.name \
            FROM states s, cities c \
            WHERE s.name = %(state)s \
              AND c.state_id = s.id \
            ORDER BY id ASC"

    cur.execute(stmt, {'state': state})
    query = cur.fetchall()
    print(", ".join([row[1] for row in query]))

    cur.close()
    conn.close()
