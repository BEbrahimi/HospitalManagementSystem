
import mysql.connector

def get_connection():
    con = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Root@gmail.com',
        port='3308',
        database='hospitalms'
    )
    return con
