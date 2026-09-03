import pandas as pd
import json 

path = './datos/clientes.json'

clientes = pd.DataFrame()
with open(path, 'r') as file:
    data = json.load(file)
    clientes = pd.DataFrame(data)

numero_clientes = clientes["id_cliente"].size
print("Numero de clientes:", numero_clientes)
print("================================")
edad_promedio = clientes["edad"].mean()
print("Edad promedio de los clientes:", edad_promedio)
print("================================")
ciudad_maxima_clientes = clientes["ciudad"].value_counts().idxmax()
print("Ciudad con mayor número de clientes:", ciudad_maxima_clientes)
print("================================")
cliente_mayor_edad = clientes.loc[clientes["edad"].idxmax()]
print("Cliente de mayor edad:")
print(cliente_mayor_edad)
print("================================")
cliente_menor_edad = clientes.loc[clientes["edad"].idxmin()]
print("Cliente de menor edad:")
print(cliente_menor_edad)
print("================================")