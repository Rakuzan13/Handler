import pandas as pd

def transform(file_path):
    df=pd.read_csv(file_path)
    df=df.dropna()
    df["Year"]=df["Year"].astype(int)
    df.reset_index(drop=True, inplace=True)
    df.to_csv(file_path,index=False)
    return df
transform(file_path="processed/cleaned_video_game_sales.csv")

