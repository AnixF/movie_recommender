import sqlite3

connection = sqlite3.connect('movies.db')
cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS movies (id INTEGER PRIMARY KEY AUTOINCREMENT, title VARCHAR, genre VARCHAR) ")
cursor.execute("CREATE TABLE IF NOT EXISTS ratings (id INTEGER PRIMARY KEY AUTOINCREMENT, movie_id INTEGER, user_id INTEGER, rating INTEGER) ")

fork = int(input("Поиск по жанру - 1 \nПоказать топ 3 - 2: \n"))

if fork == 1:
    user_genre = input("Введите жанр: ")
    cursor.execute(f"SELECT movies.genre, AVG(ratings.rating) FROM movies JOIN ratings ON movies.id = ratings.movie_id WHERE movies.genre = '{user_genre}'")
    print(cursor.fetchall())
elif fork == 2:
    cursor.execute("SELECT movies.title, AVG(ratings.rating) FROM movies JOIN ratings ON movies.id = ratings.movie_id GROUP BY movies.title ORDER BY ratings.rating DESC LIMIT 3")
    print(cursor.fetchall())
connection.commit()
connection.close()
input()