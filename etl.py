import pandas as pd
import csv
df=pd.read_csv("data/e_commerce.csv")

del df["shipping_method"]
df.to_csv("processed/data1",index=False)

print(df)