import pandas as pd

df=pd.read_csv("processed/anime_dataset_cleaned.csv")


df=df.dropna()

df.drop(columns=["url"],inplace=True)
df.drop(columns=["synopsis"],inplace=True)
df.drop(columns=["favorites"],inplace=True)
df.drop(columns=["airing"],inplace=True)
df.drop(columns=["title"],inplace=True)
df.rename(columns={"title_english":"title"},inplace=True)


df["episodes"] = df["episodes"].astype(int)
df["rank"] = df["rank"].astype(int)
df["year"] = df["year"].astype(int)

df=df.reset_index(drop=True)

print(df.columns)
print(df.status.head())

df.to_csv("processed/anime_dataset_cleaned.csv",index=False)

