import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="telecom"
)

cursor=db.cursor()

class Database:
    def signup(self, data):
        print(data);