import pandas as pd
import sqlite3

for chunk in pd.read_csv("processed/cars_cleaned.csv", chunksize=50000):
    chunk.dropna(inplace=True)

    with sqlite3.connect("all_cars.db") as conn:
        chunk.to_sql("cars",conn,if_exists="append",index=False)