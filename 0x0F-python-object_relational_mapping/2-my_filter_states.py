#!/usr/bin/python3
"""
Implements a script that takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    username, password, database, name = sys.argv[1:5]
    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        password=password,
        db=database,
        charset="utf8",
    )
    cursor = connection.cursor()
    cursor.execute(
        "\
                   SELECT * FROM states \
                   WHERE name = '{}' \
                   ORDER BY id ASC".format(name)
    )
    query_rows = cursor.fetchall()
    for row in query_rows:
        print(row)
    cursor.close()
    connection.close()
