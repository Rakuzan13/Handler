import pandas as pd
import sqlite3

for chunk in pd.read_csv("processed/anime_dataset_cleaned.csv", chunksize=50000):
    chunk.dropna(inplace=True)

    with sqlite3.connect("top_anime.db") as conn:
        chunk.to_sql("anime",conn,if_exists="append",index=False)