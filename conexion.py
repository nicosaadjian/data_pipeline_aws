import pyodbc

# Datos de conexión
server   = "..."  # endpoint + puerto
database = "..."                                          # base de datos
username = "..."                                            # usuario maestro
password = "..."

# Conexión ODBC
conn = pyodbc.connect(
    f"DRIVER={{ODBC Driver 17 for SQL Server}};"
    f"SERVER={server};"
    f"DATABASE={database};"
    f"UID={username};"
    f"PWD={password}"
)




conn.close()
