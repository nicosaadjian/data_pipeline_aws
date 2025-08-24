import pandas as pd
from scripts.common_utils import extract_csv_data, transform_metro_data

# el error del interpreter lo pude resolver agregando el path del interpreter a settings.json y borrando la parte de data_pipeline al inicio del import

def run_metro_pipeline():

    subte_csv = r'C:\Users\nicos\OneDrive\Escritorio\data_pipeline\data\bocas-de-subte.csv'

    rename_dict = {
    'long': 'Longitud', 
    'lat' : 'Latitud', 
    'id'  : 'Id', 
    'linea': 'Linea', 
    'estacion': 'Estacion', 
    'numero_de_': 'Numero_De', 
    'destino_bo' : 'Destino_Bo',
    'lineas_de_' : 'Lineas_De', 
    'cierra_fin' : 'Cierra_Fin', 
    'escalera_p' : 'Escalera_P', 
    'escalera_m' : 'Escalera_M', 
    'ascensor' : 'Ascensor',
    'rampa' : 'Rampa', 
    'salvaescal' : 'SalvaEscalera', 
    'calle' : 'Calle', 
    'altura' : 'Altura', 
    'calle2' : 'Calle2', 
    'barrio' : 'Barrio', 
    'comuna' : 'Columna',
    'observacio' : 'Observacion', 
    'Objeto' : 'Objeto', 
    'dom_norma' : 'Dom_Norma', 
    'dom_orig' : 'Dom_Origin'
}

    df = extract_csv_data(subte_csv)
    df = transform_metro_data(df, rename_dict)
    
    return df

if __name__ == 'main':
    df = run_metro_pipeline()