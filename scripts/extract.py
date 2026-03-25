import pandas as pd
import csv

df=pd.read_csv("data/cars_dataset.csv")

print(df.head(3))
print(df.tail(3))

df.to_csv("processed/cars_cleaned.csv",index=False)