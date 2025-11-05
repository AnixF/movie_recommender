import sqlite3


connection = sqlite3.connect('movies.db')
cursor = connection.cursor()

def search_by_genre():
    user_genre = input("Введите жанр: ")
    return cursor.execute(f"SELECT movies.genre, AVG(ratings.rating) FROM movies JOIN ratings ON movies.id = ratings.movie_id WHERE movies.genre = '{user_genre}'").fetchall()
    
def get_selection():
    return cursor.execute("SELECT movies.title, AVG(ratings.rating) FROM movies JOIN ratings ON movies.id = ratings.movie_id GROUP BY movies.title ORDER BY AVG(ratings.rating) DESC LIMIT 3").fetchall()


cursor.execute("CREATE TABLE IF NOT EXISTS movies (id INTEGER PRIMARY KEY AUTOINCREMENT, title VARCHAR, genre VARCHAR) ")
cursor.execute("CREATE TABLE IF NOT EXISTS ratings (id INTEGER PRIMARY KEY AUTOINCREMENT, movie_id INTEGER, user_id INTEGER, rating INTEGER) ")

fork = int(input("Поиск по жанру - 1 \nПоказать топ 3 - 2: \n"))

if fork == 1:
    print(search_by_genre())
elif fork == 2:
    print(get_selection())

connection.commit()
connection.close()
