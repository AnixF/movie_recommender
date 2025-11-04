import sqlite3

connection = sqlite3.connect("movies.db")
cursor = connection.cursor()

cursor.execute("SELECT movies.genre, AVG(ratings.rating) FROM movies JOIN ratings ON movies.id = ratings.movie_id GROUP BY movies.genre")
print(cursor.fetchall())

connection.commit()
connection.close()