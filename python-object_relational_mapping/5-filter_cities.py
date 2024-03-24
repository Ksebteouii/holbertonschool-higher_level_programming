#!/usr/bin/python3
"""
lists all cities of that state, using the
database hbtn_0e_4_usa
"""

import MySQLdb
import sys


def main(username, passsword, db_name, state_name):
    """
    lists all cities of that state
    """

    db = MySQLdb.connect(
        host="localhost", user=username,
        port=3306, passwd=passsword, db=db_name
    )
    cur = db.cursor()

    cur.execute(
        """
        SELECT cities.id,
        cities.name FROM \
cities JOIN states ON \
cities.state_id = states.id \
WHERE states.name = %(name)s ORDER BY \
cities.id ASC;
        """,
        {"name": state_name},
    )
    rows = cur.fetchall()

    if rows is not None:
        print(", ".join([row[1] for row in rows]))


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]
    main(username, password, db_name, state_name)
