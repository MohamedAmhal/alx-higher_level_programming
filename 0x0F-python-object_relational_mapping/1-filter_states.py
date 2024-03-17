#!/usr/bin/python3
"""list all the elements from databases strating with N"""
import MYSQLdb
import sys


if __name__ == "__main__":
    db = MYSQLdb.connect(host="localhost", user=sys.argv[1],
             passwd=sys.argv[2], db=sys.argv[3], port=3306)

    c = db.cursor()
    c.execute("""SELECT * FROM states WHERE name 
             LIKE BINARY 'N%' ORDER BY states.id""")
    lignes = c.fetchall()
    for ligne in lignes:
        print(ligne)

    c.close()
    db.close
