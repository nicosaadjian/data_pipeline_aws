import pandas as pd

# utils
def rename_df(df, rename_dict):
    df.rename(columns=rename_dict, inplace=True)
    return df

# extractor

def extract_csv_data(csv):
    df = pd.read_csv(csv)
    return df

# transformer
def transform_metro_data(df, rename_dict):
    print("Estoy dentro del transformer!!!")
    df = df.copy()
    
    rename_df(df, rename_dict)

    cols_to_keep = ['Id', 'Estacion', 'Barrio', 'Calle', 'Ascensor']

    df = df[cols_to_keep]
    
    return df

# loader
# definir el loader con snowflake connector o similar