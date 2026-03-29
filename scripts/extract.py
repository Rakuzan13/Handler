import pandas as pd
import csv

def extract(file_path,next_path):
    #this function take the data file and copy it to another path
    df=pd.read_csv(file_path)
    df.to_csv(next_path,index=False)
    return df
print(extract(file_path="data/video_game_sales.csv",next_path="processed/cleaned_video_game_sales.csv"))