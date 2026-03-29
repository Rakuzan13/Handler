import pandas as pd
import sqlite3
def load(file_path,database,table_name):
    for chunk in pd.read_csv(file_path, chunksize=50000):
        chunk.dropna(inplace=True)

    with sqlite3.connect(database) as conn:
        chunk.to_sql(table_name,conn,if_exists="append",index=False) # type: ignore

load(
    file_path="processed/cleaned_video_game_sales.csv",
    database="database/video_game_sale.db",
    table_name="video_game"
)