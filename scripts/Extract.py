import pandas as pd

def extract(path):
    df=pd.read_csv(path,encoding="utf-8", low_memory=False)
    return df

#la lecture du fichier se fait uniquement dans le extract et ceux dans une fonction sinon ce n'est pas clean