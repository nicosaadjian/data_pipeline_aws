from scripts.common_utils import extract_transform_load
from utils.conexion import connect_to_sql_server
from utils.credentials import server, database, username, password

# el error del interpreter lo pude resolver agregando el path del interpreter a settings.json y borrando la parte de data_pipeline al inicio del import

def run_metro_pipeline():

    connect_to_sql_server(server, database, username, password)

    subte_csv = r'C:\\Users\\nicos\\Desktop\\pruebas_aws\\data_pipeline_aws\data\bocas-de-subte.csv'
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
            'comuna' : 'Comuna',
            'observacio' : 'Observacion', 
            'Objeto' : 'Objeto', 
            'dom_norma' : 'Dom_Norma', 
            'dom_orig' : 'Dom_Origin'
        }

    
    extract_transform_load(subte_csv, rename_dict)

    


if __name__ == 'main':
    run_metro_pipeline()