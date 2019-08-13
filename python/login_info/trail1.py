import mysql.connector

mydb = mysql.connector.connect(
    host="localhost"
    user="myusername"
    passwd="mypassword_notReally"
    database="mydatabase"
)
print("mydb")
    
