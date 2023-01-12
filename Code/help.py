from pathlib import Path
import mysql.connector

def absPath(current, *args):
    parent = Path(current).parent
    for i in args:
        parent = parent / i
    return str(parent)


def dbcon():
    mydb = mysql.connector.connect(host = "localhost", user = "root",passwd="boop",database="booking")
    return mydb,mydb.cursor()

