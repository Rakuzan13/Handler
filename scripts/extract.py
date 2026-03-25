import pandas as pd
import csv

df=pd.read_csv("data/top_anime_dataset.csv")

print(df.head(3))
print(df.tail(3))

df.to_csv("processed/anime_dataset_cleaned.csv",index=False)

