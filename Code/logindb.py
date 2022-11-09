import mysql.connector

def dbcon():
    mydb = mysql.connector.connect(host = "localhost", user = "root",passwd="boop",database="taxi")
    return mydb,mydb.cursor()


