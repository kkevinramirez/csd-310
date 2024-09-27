import mysql.connector
from mysql.connector import errorcode

config = {
    user = 'root',
    password = 'Az34!6kBw',
    host = '3306',
    database = 'movie_queries',
    raise_on_warnings = True,
}

# Create a cursor object
cursor = db.cursor()


cursor.execute("SELECT * FROM studio;")
studios = cursor.fetchall()
print("-- DISPLAYING Studio RECORDS --")
for studio in studios:
    print(f"Studio ID: {studio[0]}")
    print(f"Studio Name: {studio[1]}")

cursor.execute("SELECT * FROM genre;")
genres = cursor.fetchall()
print("\n-- DISPLAYING Genre RECORDS --")
for genre in genres:
    print(f"Genre ID: {genre[0]}")
    print(f"Genre Name: {genre[1]}")

cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime < 120;")
short_movies = cursor.fetchall()
print("\n-- DISPLAYING Short Film RECORDS --")
for movie in short_movies:
    print(f"Film Name: {movie[0]}")
    print(f"Runtime: {movie[1]}")

cursor.execute("SELECT film_name, film_director FROM film ORDER BY film_director;")
directors_movies = cursor.fetchall()
print("\n-- DISPLAYING Director RECORDS in Order --")
for movie, director in directors_movies:
    print(f"Film Name: {movie}")
    print(f"Director: {director}")

# Close the cursor and connection
cursor.close()
db.cursor.close()
