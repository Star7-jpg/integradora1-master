import mysql.connector

def get_connection():
    mydb = mysql.connector.connect(
        host="localhost",
        user="admin",
        password="1234",
        database="papeleria2"
    )
    return mydb