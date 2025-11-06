import sqlite3
import matplotlib.pyplot as plt

connection = sqlite3.connect('movies.db')
cursor = connection.cursor()

def search_by_genre():
    user_genre = input("Введите жанр: ")
    return cursor.execute(f"SELECT movies.genre, AVG(ratings.rating) FROM movies JOIN ratings ON movies.id = ratings.movie_id WHERE movies.genre = '{user_genre}'").fetchall()
    
def get_selection():
    return cursor.execute("SELECT movies.title, AVG(ratings.rating) FROM movies JOIN ratings ON movies.id = ratings.movie_id GROUP BY movies.title ORDER BY AVG(ratings.rating) DESC LIMIT 3").fetchall()

def get_all():
    return cursor.execute("SELECT movies.title, AVG(ratings.rating) FROM movies JOIN ratings ON movies.id = ratings.movie_id GROUP BY movies.title ORDER BY AVG(ratings.rating)").fetchall()


cursor.execute("CREATE TABLE IF NOT EXISTS movies (id INTEGER PRIMARY KEY AUTOINCREMENT, title VARCHAR, genre VARCHAR) ")
cursor.execute("CREATE TABLE IF NOT EXISTS ratings (id INTEGER PRIMARY KEY AUTOINCREMENT, movie_id INTEGER, user_id INTEGER, rating INTEGER) ")

fork = int(input("Поиск по жанру - 1 \nПоказать топ 3 - 2\nПоказать все фильмы - 3\nВыдать график рейтингов фильмов - 4: \n"))

if fork == 1:
    print(search_by_genre())
elif fork == 2:
    print(get_selection())
elif fork == 3:
    print(get_all())
elif fork == 4:
    x = []
    y = []
    all_movies = get_all()
    for i in all_movies:
        x.append(i[0])
        y.append(i[1])
    plt.title("Рейтинги фильмов")
    plt.plot(x, y)
    plt.show()

connection.commit()
connection.close()
