import pandas as pd

df=pd.read_csv("processed/cars_cleaned.csv")

print(df.dtypes)

df["price"]=df["price"].astype(float)

df["price_hors_taxe"]=(df["price"]/df["tax"]).round(2)

df.rename(columns={'Make':'brand'},inplace=True)

print(df.groupby('brand')['tax'].sum())

print(df.head(3))
print(df.tail(3))
