import pandas as pd 
from sqlalchemy import create_engine
pd.set_option('display.float_format','{:.2f}'.format)
df=pd.read_csv("processed/tmdb.csv")

print(df.shape)
print(df.head(7))
print(df.tail(7))

def load(df):
    engine=create_engine("mysql+pymysql://root:password@localhost:3306/tmdb_movies")

    df.to_sql(
        name="movies",
        con=engine,
        if_exists="replace",
        index=False
    )
print("loading...done✅")