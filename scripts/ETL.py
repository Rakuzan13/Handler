import pandas as pd 
pd.set_option("display.max_columns",None)
df=pd.read_csv("data/crime_incidents_messy.csv",encoding="utf-8")

df.columns=df.columns.str.lower().str.replace(" ","_")

def drop_columns(df,columns:list):
    return df.drop(columns=columns)

def combine_name(df, fisrt_name_col,last_name_col, fullname):
    df[fullname]=(df[fisrt_name_col].fillna("").str.strip()+ " "+df[last_name_col].fillna("").str.strip()).str.strip()
    return df

df=combine_name(df,"officer_first_name","officer_last_name","officer_name")
df=combine_name(df,"suspect_first_name","suspect_last_name","suspect_name")
df=combine_name(df,"victim_first_name","victim_last_name","victim_name")

column=["latitude","longitude","victim_phone","notes","officer_first_name"
        ,"suspect_first_name","suspect_last_name","victim_first_name","victim_last_name","badge_number"
        ]
df=drop_columns(df,column)

print(df["crime_type"].unique)
"""print(df.head())"""
