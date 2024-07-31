# your code here
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json
import sqlite3
import pandas as pd
url_movies = "https://raw.githubusercontent.com/4GeeksAcademy/k-nearest-neighbors-project-tutorial/main/tmdb_5000_movies.csv"
url_credits = "https://raw.githubusercontent.com/4GeeksAcademy/k-nearest-neighbors-project-tutorial/main/tmdb_5000_credits.csv"

ssl_context_movies = urllib.request.urlopen(url_movies, context=ssl._create_unverified_context())
ssl_context_credits = urllib.request.urlopen(url_credits, context=ssl._create_unverified_context())

df_movies = pd.read_csv(ssl_context_movies, index_col=None)
df_credits = pd.read_csv(ssl_context_credits, index_col=None)

df_movies.to_csv('../data/raw/movies-data.csv', index = False)
df_credits.to_csv('../data/raw/credits-movie.csv', index = False)

print(data_movies)
print(data_credits)
# # Print the columns of the DataFrames
# print("data_movies columns:", data_movies.columns)
# print("data_credits columns:", data_credits.columns)
# # Ensure 'id' column exists in data_movies
# if 'id' not in data_movies.columns:
#     print("Error: 'id' column not found in data_movies")
# else:
#     print("'id' column found in data_movies")
# # Ensure 'title' column exists in both DataFrames
# if 'title' not in data_movies.columns or 'title' not in data_credits.columns:
#     print("Error: 'title' column not found in one or both DataFrames")
# else:
#     print("'title' column found in both DataFrames")
# Connect to SQLite database (or create it)
conn = sqlite3.connect('movies.db')
# Store DataFrames in separate tables
data_movies.to_sql('table_movies', conn, if_exists='replace', index=False)
data_credits.to_sql('table_credits', conn, if_exists='replace', index=False)
# SQL query to join the tables on the 'title' column
query = '''
SELECT table_movies.id AS movie_id, table_movies.title, table_movies.overview, table_movies.genres, table_movies.keywords,
       table_credits.cast, table_credits.crew
FROM table_movies
JOIN table_credits ON table_movies.title = table_credits.title
'''
# Execute the query and load the result into a DataFrame
try:
    unified_df = pd.read_sql_query(query, conn)
    print("Unified DataFrame created successfully")
    # print(unified_df)
except Exception as e:
    print("Error executing query:", e)
# Close the database connection
conn.close()