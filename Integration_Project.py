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

comentarios = pd.read_csv('./datos/comentarios.txt', sep=r'\|', engine='python', skiprows=[1])
comentarios.columns = comentarios.columns.str.strip()

comentarios["Sentimiento"] = comentarios["Sentimiento"].str.strip()

comentarios_positivos = comentarios[comentarios["Sentimiento"] == "Bueno"]

comentarios_negativos = comentarios[comentarios["Sentimiento"] == "Malo"]

porcentaje_positivo = (comentarios_positivos.shape[0] / comentarios.shape[0]) * 100

comentarios["Comentario"] = comentarios["Comentario"].str.strip()

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
    "cli_ciudad", 
    "cantidad",      
    "prod_precio",   
    "importe",
    "fecha"            
]

clear_merge = df_completo[columnas_select]


clear_merge.to_excel('./datos/resultados.xlsx', index=False)


producto_mas_vendidos = clear_merge.groupby("prod_nombre")["cantidad"].sum().idxmax()
print("Producto más vendido:", producto_mas_vendidos)
producto_mayor_importe = clear_merge.groupby("prod_nombre")["importe"].sum().idxmax()
print("Producto con mayor importe:", producto_mayor_importe)
cliente_mas_compras = clear_merge.groupby("cli_nombre")["id_venta"].count().idxmax()
print("Cliente con más compras:", cliente_mas_compras)
ingreso_total = clear_merge["importe"].sum()
print("Ingreso total:", ingreso_total)
categoria_mas_vendida = clear_merge.groupby("prod_categoria")["importe"].sum().idxmax()
print("Categoría con mayor ingreso:", categoria_mas_vendida)
ciudad_mas_clientes = clientes.groupby("ciudad")["id_cliente"].count().idxmax()
print("Ciudad con más clientes:", ciudad_mas_clientes)
print("Porcentaje de comentarios positivos:", porcentaje_positivo,"%")
problema_mayor_frecuencia = comentarios_negativos["Comentario"].value_counts().idxmax()
print("Problema con mayor frecuencia:", problema_mayor_frecuencia)