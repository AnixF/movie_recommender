import sqlite3

connection = sqlite3.connect('movies.db')
cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS movies (id INTEGER PRIMARY KEY AUTOINCREMENT, title VARCHAR, genre VARCHAR) ")
cursor.execute("CREATE TABLE IF NOT EXISTS ratings (id INTEGER PRIMARY KEY AUTOINCREMENT, movie_id INTEGER, user_id INTEGER, rating INTEGER) ")
connection.commit()
connection.close()
input()