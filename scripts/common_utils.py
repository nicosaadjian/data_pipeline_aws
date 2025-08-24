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

def load_data_to_aws_rds(df, conn):
    # insert into tempdb.dbo.test_table(df) ---> write_pandas.tools
    # Implementar la lógica para cargar el DataFrame en Snowflake usando el conector proporcionado
    pass

def extract_transform_load(csv_file, rename_dict, conn):
    print("Beginning ETL process: extracting data from CSV.\n")
    df = extract_csv_data(csv_file)
    print("ETL process: transforming data from CSV.\n")
    df = transform_metro_data(df, rename_dict)
    print("Ending ETL process: inserting transformed data from CSV into AWS RDS.\n")
    load_data_to_aws_rds(df, conn)
    
    return df