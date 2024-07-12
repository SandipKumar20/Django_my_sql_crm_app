import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="pwd123"
)

cursorObject = database.cursor()
cursorObject.execute("CREATE DATABASE timeco")

print("All Done!")