import pyodbc

# Conexión ODBC

def connect_to_sql_server(server, database, username, password):
    conn = pyodbc.connect(
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={server};"
        f"DATABASE={database};"
        f"UID={username};"
        f"PWD={password}"
    )




# conn.close()
