import pandas as pd 
pd.set_option("display.max_columns",None)

input_file = "data/raw/crime_incidents.csv"
output_file = "data/processed/crime_incidents_clean.csv"

df=pd.read_csv("data/crime_incidents_messy.csv",encoding="utf-8")

df.columns=df.columns.str.lower().str.replace(" ","_")

#functions reusable to drop columns 
def drop_columns(df,columns:list):
    return df.drop(columns=columns)


# functions to combine names a
def combine_name(df, fisrt_name_col,last_name_col, fullname):
    df[fullname]=(df[fisrt_name_col].fillna("").str.strip()+" "+df[last_name_col].fillna("").str.strip()).str.strip()
    return df
df=combine_name(df,"officer_first_name","officer_last_name","officer_name")
df=combine_name(df,"suspect_first_name","suspect_last_name","suspect_name")
df=combine_name(df,"victim_first_name","victim_last_name","victim_name")

column=["latitude","longitude","victim_phone","notes","officer_first_name"
        ,"suspect_first_name","suspect_last_name","victim_first_name","victim_last_name","badge_number"
        ]
df=drop_columns(df,column)

#we gonna clean columns like crime_type and many others...
df["crime_type"]=df["crime_type"].str.replace("  "," ")

df["crime_type"]=df["crime_type"].replace({
    "asslt":"assault",
    "burglry":"buglary",
    "b&e":"breaking & entering",
    "arsen":"arson",
    "trespass":"trespassing",
    "robbry":"robbery",
    "dv":"domestic violence",
    "domestc violence":"domestic violence",
    "sa":"sexual assualt",
    "cyber crime":"cybercrime",
    "larceny":"theft/larceny",
    "homocide":"homicide"
})


#should find a way to remove dwi ,duii ,d.u.i for dui
spell=lambda x: "dui" if x in ("dwi" ,"duii" ,"d.u.i") else 0
df["crime_type"]=df["crime_type"].map(spell)


df["district"]=df["district"].replace({
    "sou":"south",
    "cen":"central",
    "nor":"north",
    "mid":"midtown",
    "wes":"west",
    "eas":"east"
})


df["suspect_gender"]=df["suspect_gender"].str.strip()

print(df.head())
print(df["crime_type"].unique())
