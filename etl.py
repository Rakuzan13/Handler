import pandas as pd
import csv
df=pd.read_csv("data/tmdb_movies.csv")

del df["release_date"]
del df["runtime"]
df["vote_average"]=df["vote_average"].round(2)
df["revenue"]=(df["revenue"]/1_000_000).round(5)

df.rename(columns={"revenue":"revenue_usd","budget":"budget_usd" },inplace=True)

print(df.head())
print(df.tail())
df.to_csv("processed/clean_tmdb_movies.csv",index=False)