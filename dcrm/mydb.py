import mysql.connector

db = mysql.connector.connect(
	host='localhost',
	user='root',
	passwd='hA78.21bx/91-gB427k'
)

cursor = db.cursor()

cursor.execute('''CREATE DATABASE advancedb''')