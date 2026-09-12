import pandas as pd 
pd.set_option("display.max_columns",None)
df=pd.read_csv("data/crime_incidents_messy.csv",encoding="utf-8")

df.columns=df.columns.str.lower().str.replace(" ","_")
def drop_columns(df,columns:list):
    return df.drop(columns=columns)

column=["latitude","longitude","victim_phone","notes"]
drop_columns(df,column)

print(df.columns)