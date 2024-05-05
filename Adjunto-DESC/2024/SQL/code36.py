import sqlite3
import json

# Load Pixar movies data from a JSON file.
with open("pixar_movies.json", "r") as file:
    pixar_movies = json.load(file)

################################################

# Connect to a SQLite database or create it if it doesn't exist.
conn = sqlite3.connect("pixar_movies.db")

# Create a 'Movies' table if it does not exist in the database.
conn.execute("""
CREATE TABLE IF NOT EXISTS Movies (
    id INTEGER PRIMARY KEY, 
    title TEXT NOT NULL, 
    year INTEGER NOT NULL
)
""")

# Insert movie data into the 'Movies' table using executemany to handle multiple entries efficiently.
conn.executemany("INSERT INTO Movies VALUES (:id, :title, :year)", pixar_movies)

# Commit changes to save them in the database, then close the connection to release resources.
conn.commit()
conn.close()

################################################

# Reconnect to the database to perform queries.
conn = sqlite3.connect("pixar_movies.db")
cursor = conn.cursor()

# Query to fetch all movies stored in the database.
cursor.execute("SELECT * FROM Movies")
movies = cursor.fetchall()
for movie in movies:
    print(movie)

###############SOLOS###################

# Query to find movies released after 2010.
cursor.execute("SELECT * FROM Movies WHERE year > 2010")
recent_movies = cursor.fetchall()
for movie in recent_movies:
    print(movie)

################################################

# Load viewer data from another JSON file to simulate users who have watched the movies.
with open("movie_viewers.json", "r") as file:
    movie_viewers = json.load(file)

# Create 'MovieViewers' table to store data about viewers.
conn.execute("""
CREATE TABLE IF NOT EXISTS MovieViewers (
    id INTEGER PRIMARY KEY, 
    movie_id INTEGER NOT NULL, 
    name TEXT NOT NULL, 
    last_name TEXT NOT NULL, 
    FOREIGN KEY (movie_id) REFERENCES Movies(id)
)
""")

# Insert viewer data into 'MovieViewers' table.
conn.executemany("INSERT INTO MovieViewers VALUES (:id, :movie_id, :name, :last_name)", movie_viewers)
conn.commit()

################################################
movie_title = "Toy Story"
# Query using INNER JOIN to fetch viewers for the movie 'Toy Story'.
cursor.execute("""
SELECT MovieViewers.name, MovieViewers.last_name 
FROM Movies 
INNER JOIN MovieViewers ON Movies.id = MovieViewers.movie_id 
WHERE Movies.title = ?
""", movie_title)

viewers = cursor.fetchall()
for viewer in viewers:
    print(viewer)

# Close the database connection to ensure all resources are properly released.
conn.close()
