import pandas as pd 
pd.set_option("display.max_columns",None)
df=pd.read_csv("data/crime_incidents_messy.csv",encoding="utf-8")

"""print(df.head())
print(df.shape)
print(df.info())
print(df.isnull().sum())
print(df.duplicated().sum())
print(df.columns)"""

df.columns=df.columns.str.lower().str.replace(" ","_")
print(df.columns)
