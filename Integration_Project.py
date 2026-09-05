import pandas as pd
from sqlalchemy import create_engine

USER = "root"
PASSWORD = "rootpassword"
HOST = "127.0.0.1"
PORT = "3306"
DATABASE = "tienda_db"

connection_uri = f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
engine = create_engine(connection_uri)

productos = pd.read_sql_table("Productos", con=engine)
clientes = pd.read_json('./datos/clientes.json')
ventas = pd.read_csv('./datos/ventas.csv')


ventas["importe"] = ventas["precio_unitario"] * ventas["cantidad"]

clientes_pref = clientes.set_index("id_cliente").add_prefix("cli_").reset_index()
productos_pref = productos.set_index("id_producto").add_prefix("prod_").reset_index()



df_completo = (
    ventas
    .merge(clientes_pref, on="id_cliente", how="inner")
    .merge(productos_pref, on="id_producto", how="inner")
)


columnas_select = [
    "id_venta",         
    "prod_nombre",
    "prod_categoria",
    "cli_nombre", 
    "cantidad",      
    "prod_precio",   
    "importe",
    "fecha"            
]

clear_merge = df_completo[columnas_select]

print("Merge completo de ventas, clientes y productos:")
print(clear_merge)


clear_merge.to_excel('./datos/resultados.xlsx', index=False)