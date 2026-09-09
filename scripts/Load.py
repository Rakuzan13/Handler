import sqlite3 
import pandas as pd 

def load(df,db_name="Airbnb.db"):
    conn=sqlite3.connect(f"database/{db_name}")

    #load all of my tables
    df.to_sql("Airbnb",conn,if_exists="replace",index=False)
    conn.close()
    print("chagement terminé ✅")