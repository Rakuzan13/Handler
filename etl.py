import pandas as pd
import csv
df=pd.read_csv("data/tmdb_movies.csv")

dfs=df.copy()

df["vote_average"]=df["vote_average"].round(3)

dfs.to_csv("processed/tmdb.csv",float_format="%.2f",index=False)
