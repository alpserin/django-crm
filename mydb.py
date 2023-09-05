import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "password123"
)

# prepare a cursor object
cursorObject = dataBase.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE mydb")
print("All done!")

